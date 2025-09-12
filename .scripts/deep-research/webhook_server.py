#!/usr/bin/env python3
"""
Webhook server for OpenAI Deep Research with signature verification
Handles async callbacks from OpenAI's Deep Research API
"""

import os
import json
import time
import queue
import threading
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from flask import Flask, request, jsonify
from openai import OpenAI
import sqlite3
import hashlib

# Configuration
WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT", "8080"))
DB_PATH = Path.home() / ".deep-research" / "tasks.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Initialize Flask app
app = Flask(__name__)

# Task queue for async processing
task_queue = queue.Queue()

# Track processed webhooks for idempotency
processed_webhooks = set()

# OpenAI client for webhook verification
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TaskDatabase:
    """SQLite database for tracking research tasks"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database schema"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    model TEXT,
                    query TEXT,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    completed_at TIMESTAMP,
                    output_file TEXT,
                    error TEXT,
                    metadata TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS webhook_events (
                    webhook_id TEXT PRIMARY KEY,
                    task_id TEXT,
                    received_at TIMESTAMP,
                    processed_at TIMESTAMP,
                    raw_data TEXT,
                    FOREIGN KEY (task_id) REFERENCES tasks(id)
                )
            """)
            conn.commit()
    
    def create_task(self, task_id: str, model: str, query: str, metadata: Dict = None):
        """Create a new task record"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO tasks (id, status, model, query, created_at, updated_at, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                task_id,
                "pending",
                model,
                query,
                datetime.now(),
                datetime.now(),
                json.dumps(metadata or {})
            ))
            conn.commit()
    
    def update_task_status(self, task_id: str, status: str, output_file: str = None, error: str = None):
        """Update task status"""
        with sqlite3.connect(self.db_path) as conn:
            completed_at = datetime.now() if status == "completed" else None
            conn.execute("""
                UPDATE tasks 
                SET status = ?, updated_at = ?, completed_at = ?, output_file = ?, error = ?
                WHERE id = ?
            """, (status, datetime.now(), completed_at, output_file, error, task_id))
            conn.commit()
    
    def get_task(self, task_id: str) -> Optional[Dict]:
        """Get task details"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def list_tasks(self, limit: int = 20) -> list:
        """List recent tasks"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT id, status, model, query, created_at, completed_at 
                FROM tasks 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (limit,))
            return [dict(row) for row in cursor.fetchall()]
    
    def record_webhook(self, webhook_id: str, task_id: str, raw_data: str):
        """Record webhook event"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR IGNORE INTO webhook_events 
                (webhook_id, task_id, received_at, raw_data)
                VALUES (?, ?, ?, ?)
            """, (webhook_id, task_id, datetime.now(), raw_data))
            conn.commit()
    
    def mark_webhook_processed(self, webhook_id: str):
        """Mark webhook as processed"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                UPDATE webhook_events 
                SET processed_at = ? 
                WHERE webhook_id = ?
            """, (datetime.now(), webhook_id))
            conn.commit()

# Initialize database
db = TaskDatabase(DB_PATH)

def verify_webhook_signature(request_data: bytes, headers: dict, secret: str) -> Optional[Dict]:
    """
    Verify webhook signature using OpenAI's webhook verification
    
    Returns:
        Verified event data or None if verification fails
    """
    try:
        # OpenAI's webhook.unwrap handles signature verification
        event = client.webhooks.unwrap(
            request_data,
            headers,
            secret=secret
        )
        return event
    except Exception as e:
        print(f"❌ Webhook verification failed: {e}")
        return None

def process_research_result(event: Dict[str, Any]):
    """
    Process the research result and save to Obsidian
    Runs in background thread from queue
    """
    try:
        task_id = event.get('id')
        print(f"📝 Processing research result: {task_id}")
        
        # Extract output
        output_text = event.get('output_text', '')
        
        # Save to Obsidian vault
        output_file = save_to_obsidian(task_id, event)
        
        # Update database
        db.update_task_status(
            task_id=task_id,
            status="completed",
            output_file=str(output_file)
        )
        
        print(f"✅ Research saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error processing result: {e}")
        db.update_task_status(
            task_id=event.get('id'),
            status="error",
            error=str(e)
        )

def save_to_obsidian(task_id: str, event: Dict) -> Path:
    """Save research results to Obsidian vault"""
    from pathlib import Path
    
    OBSIDIAN_DIR = Path.home() / "dev" / "02_Areas" / "Obsidian" / "00 Inbox" / "Deep Research"
    OBSIDIAN_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    # Get task info from database
    task_info = db.get_task(task_id)
    query_preview = task_info['query'][:50] if task_info else "Research"
    
    # Clean query for filename
    safe_query = "".join(c for c in query_preview if c.isalnum() or c in " -_").strip()
    filename = f"{timestamp} - {safe_query}.md"
    filepath = OBSIDIAN_DIR / filename
    
    # Build content with frontmatter
    content = "---\n"
    content += f"title: Deep Research - {safe_query}\n"
    content += f"date: {datetime.now().isoformat()}\n"
    content += f"task_id: {task_id}\n"
    content += f"model: {task_info.get('model', 'unknown')}\n"
    content += f"status: completed\n"
    content += "tags: [deep-research, ai-generated]\n"
    content += "---\n\n"
    
    # Add main content
    content += f"# {safe_query}\n\n"
    
    # Add the research output
    output_text = event.get('output_text', '')
    content += output_text
    
    # Add research process details
    if 'output' in event:
        content += "\n\n---\n\n## Research Process\n\n"
        
        web_searches = []
        code_executions = []
        
        for item in event.get('output', []):
            item_type = item.get('type')
            
            if item_type == 'web_search_call':
                action = item.get('action', {})
                action_type = action.get('type')
                
                if action_type == 'search':
                    web_searches.append(f"- Searched: \"{action.get('query', 'N/A')}\"")
                elif action_type == 'open_page':
                    web_searches.append(f"- Opened: {action.get('url', 'N/A')}")
            
            elif item_type == 'code_interpreter_call':
                code_executions.append(f"- Executed code block")
        
        if web_searches:
            content += "### Web Searches\n\n"
            content += "\n".join(web_searches) + "\n\n"
        
        if code_executions:
            content += "### Code Execution\n\n"
            content += "\n".join(code_executions) + "\n\n"
    
    # Write file
    filepath.write_text(content)
    return filepath

def worker_thread():
    """Background worker to process queued tasks"""
    while True:
        try:
            event = task_queue.get(timeout=1)
            process_research_result(event)
            task_queue.task_done()
        except queue.Empty:
            continue
        except Exception as e:
            print(f"❌ Worker error: {e}")

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    """
    Handle webhook callbacks from OpenAI
    Implements signature verification and idempotency
    """
    try:
        # Get webhook secret from environment
        webhook_secret = os.getenv("OPENAI_WEBHOOK_SECRET")
        if not webhook_secret:
            print("⚠️  Warning: OPENAI_WEBHOOK_SECRET not set, skipping verification")
            event = request.json
        else:
            # Verify webhook signature
            event = verify_webhook_signature(
                request.data,
                dict(request.headers),
                webhook_secret
            )
            
            if not event:
                return jsonify({"error": "Invalid signature"}), 401
        
        # Check idempotency using webhook-id header
        webhook_id = request.headers.get('webhook-id', hashlib.md5(request.data).hexdigest())
        
        if webhook_id in processed_webhooks:
            print(f"⚠️  Duplicate webhook: {webhook_id}")
            return '', 200  # Already processed
        
        processed_webhooks.add(webhook_id)
        
        # Record webhook event
        task_id = event.get('id')
        db.record_webhook(webhook_id, task_id, json.dumps(event))
        
        # Queue for async processing
        task_queue.put(event)
        
        # Mark as received
        db.mark_webhook_processed(webhook_id)
        
        print(f"✅ Webhook received for task: {task_id}")
        
        # Return 200 immediately as required by OpenAI
        return '', 200
        
    except Exception as e:
        print(f"❌ Webhook handler error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/status/<task_id>', methods=['GET'])
def task_status(task_id: str):
    """Get status of a research task"""
    task = db.get_task(task_id)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['GET'])
def list_tasks():
    """List recent research tasks"""
    limit = request.args.get('limit', 20, type=int)
    tasks = db.list_tasks(limit)
    return jsonify(tasks), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "queue_size": task_queue.qsize(),
        "processed_webhooks": len(processed_webhooks)
    }), 200

def start_server():
    """Start the webhook server with worker thread"""
    # Start worker thread
    worker = threading.Thread(target=worker_thread, daemon=True)
    worker.start()
    print(f"✅ Worker thread started")
    
    # Start Flask server
    print(f"🚀 Starting webhook server on port {WEBHOOK_PORT}")
    print(f"📁 Database: {DB_PATH}")
    app.run(host='0.0.0.0', port=WEBHOOK_PORT, debug=False)

if __name__ == "__main__":
    start_server()