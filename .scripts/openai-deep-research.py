#!/usr/bin/env python3
"""
OpenAI Deep Research Integration for Claude Code
Allows running OpenAI's deep research models through Claude Code
"""

import os
import sys
import json
import time
import argparse
import threading
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any
from flask import Flask, request, jsonify
from openai import OpenAI
import requests

# Configuration
WEBHOOK_PORT = 8080
TAILSCALE_HOSTNAME = "deep-research"
RESEARCH_OUTPUT_DIR = Path.home() / "dev" / "02_Areas" / "Obsidian" / "00 Inbox" / "Deep Research"
RESEARCH_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Flask app for webhook
app = Flask(__name__)

# Global storage for research results
research_results = {}

def setup_tailscale_serve():
    """Configure Tailscale to serve the webhook endpoint"""
    try:
        # Check if Tailscale is running
        subprocess.run(["tailscale", "status"], check=True, capture_output=True)
        
        # Set up Tailscale serve
        cmd = f"tailscale serve --bg https+insecure://localhost:{WEBHOOK_PORT}"
        subprocess.run(cmd.split(), check=True)
        
        # Get Tailscale hostname
        result = subprocess.run(
            ["tailscale", "status", "--json"], 
            capture_output=True, 
            text=True
        )
        status = json.loads(result.stdout)
        tailnet_name = status.get("MagicDNSSuffix", "")
        
        webhook_url = f"https://{TAILSCALE_HOSTNAME}.{tailnet_name}/webhook"
        print(f"✅ Webhook endpoint configured at: {webhook_url}")
        return webhook_url
    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting up Tailscale: {e}")
        return None

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    """Handle webhook callbacks from OpenAI"""
    try:
        data = request.json
        response_id = data.get('id')
        
        if response_id:
            research_results[response_id] = data
            print(f"📥 Received research result: {response_id}")
            
            # Save to file
            save_research_to_obsidian(response_id, data)
            
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "No response ID"}), 400
            
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        return jsonify({"error": str(e)}), 500

def save_research_to_obsidian(response_id: str, data: Dict[Any, Any]):
    """Save research results to Obsidian vault"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    filename = f"{timestamp} - Deep Research - {response_id[:8]}.md"
    filepath = RESEARCH_OUTPUT_DIR / filename
    
    # Extract content
    output_text = data.get('output_text', '')
    metadata = {
        'title': f"Deep Research - {response_id[:8]}",
        'date': datetime.now().isoformat(),
        'model': data.get('model', 'unknown'),
        'response_id': response_id,
        'status': data.get('status', 'unknown')
    }
    
    # Format as Obsidian note with frontmatter
    content = "---\n"
    for key, value in metadata.items():
        content += f"{key}: {value}\n"
    content += "---\n\n"
    content += f"# Deep Research Results\n\n"
    content += output_text
    
    # Add tool call history if available
    if 'output' in data:
        content += "\n\n## Research Process\n\n"
        for item in data.get('output', []):
            if item.get('type') == 'web_search_call':
                action = item.get('action', {})
                content += f"- **Web Search**: {action.get('query', 'N/A')}\n"
            elif item.get('type') == 'message':
                # Already included in output_text
                pass
    
    filepath.write_text(content)
    print(f"💾 Saved research to: {filepath}")
    return filepath

class DeepResearchClient:
    def __init__(self, api_key: Optional[str] = None, webhook_url: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required (set OPENAI_API_KEY)")
        
        self.client = OpenAI(api_key=self.api_key, timeout=3600)
        self.webhook_url = webhook_url
    
    def research(
        self, 
        query: str, 
        model: str = "o4-mini-deep-research",
        use_web_search: bool = True,
        use_code_interpreter: bool = False,
        vector_store_ids: Optional[list] = None,
        max_tool_calls: Optional[int] = None,
        background: bool = True
    ) -> Dict[str, Any]:
        """
        Execute a deep research query
        
        Args:
            query: The research question/task
            model: Model to use (o3-deep-research or o4-mini-deep-research)
            use_web_search: Enable web search tool
            use_code_interpreter: Enable code interpreter
            vector_store_ids: List of vector store IDs for file search
            max_tool_calls: Maximum number of tool calls
            background: Run in background mode
        """
        
        # Build tools list
        tools = []
        if use_web_search:
            tools.append({"type": "web_search_preview"})
        
        if vector_store_ids:
            tools.append({
                "type": "file_search",
                "vector_store_ids": vector_store_ids
            })
        
        if use_code_interpreter:
            tools.append({
                "type": "code_interpreter",
                "container": {"type": "auto"}
            })
        
        if not tools:
            raise ValueError("At least one tool must be enabled")
        
        # Create request parameters
        params = {
            "model": model,
            "input": query,
            "background": background,
            "tools": tools
        }
        
        if max_tool_calls:
            params["max_tool_calls"] = max_tool_calls
        
        if self.webhook_url and background:
            params["webhook"] = {
                "url": self.webhook_url,
                "secret": os.getenv("WEBHOOK_SECRET", "default-secret")
            }
        
        print(f"🔍 Starting deep research: {model}")
        print(f"📝 Query: {query[:100]}...")
        
        response = self.client.responses.create(**params)
        
        if background:
            print(f"✅ Research task submitted: {response.id}")
            print(f"⏳ Running in background, webhook will be called when complete")
            return {"id": response.id, "status": "running", "background": True}
        else:
            # Save results immediately for non-background mode
            result = {
                "id": response.id,
                "output_text": response.output_text,
                "model": model,
                "status": "completed"
            }
            filepath = save_research_to_obsidian(response.id, result)
            return {
                "id": response.id,
                "status": "completed",
                "output_file": str(filepath),
                "output_text": response.output_text[:500] + "..." if len(response.output_text) > 500 else response.output_text
            }

def run_webhook_server():
    """Run the Flask webhook server in a thread"""
    app.run(host='localhost', port=WEBHOOK_PORT, debug=False)

def main():
    parser = argparse.ArgumentParser(description='OpenAI Deep Research for Claude Code')
    parser.add_argument('query', nargs='?', help='Research query')
    parser.add_argument('--model', default='o4-mini-deep-research', 
                       choices=['o3-deep-research', 'o4-mini-deep-research'],
                       help='Model to use')
    parser.add_argument('--no-web', action='store_true', help='Disable web search')
    parser.add_argument('--code', action='store_true', help='Enable code interpreter')
    parser.add_argument('--vector-stores', nargs='+', help='Vector store IDs')
    parser.add_argument('--max-calls', type=int, help='Max tool calls')
    parser.add_argument('--foreground', action='store_true', help='Run in foreground')
    parser.add_argument('--server', action='store_true', help='Start webhook server only')
    
    args = parser.parse_args()
    
    if args.server:
        # Just run the webhook server
        webhook_url = setup_tailscale_serve()
        if webhook_url:
            print(f"🚀 Starting webhook server on port {WEBHOOK_PORT}")
            run_webhook_server()
        return
    
    if not args.query:
        print("Error: Query required (or use --server to start webhook server)")
        parser.print_help()
        sys.exit(1)
    
    # Start webhook server in background if using background mode
    webhook_url = None
    if not args.foreground:
        webhook_url = setup_tailscale_serve()
        if webhook_url:
            server_thread = threading.Thread(target=run_webhook_server, daemon=True)
            server_thread.start()
            time.sleep(2)  # Give server time to start
    
    # Initialize client and run research
    try:
        client = DeepResearchClient(webhook_url=webhook_url)
        result = client.research(
            query=args.query,
            model=args.model,
            use_web_search=not args.no_web,
            use_code_interpreter=args.code,
            vector_store_ids=args.vector_stores,
            max_tool_calls=args.max_calls,
            background=not args.foreground
        )
        
        print("\n📊 Result:")
        print(json.dumps(result, indent=2))
        
        if not args.foreground:
            print("\n⏳ Research running in background. Results will be saved to Obsidian.")
            print("Press Ctrl+C to stop the webhook server")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n👋 Shutting down...")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()