# OpenAI Deep Research + Claude Code Integration Plan v3

## 🎯 Project Goal
Enable Claude Code to leverage OpenAI's Deep Research models for complex, multi-step research tasks with results automatically saved to Obsidian vault.

## ⚠️ Critical Corrections from v2
1. **Use Tailscale Funnel, NOT Serve** - OpenAI webhooks come from public internet
2. **Use SDK's `client.webhooks.unwrap()`** - Don't implement custom HMAC
3. **Correct model IDs**: `o3-deep-research-2025-06-26` and `o4-mini-deep-research-2025-06-26`
4. **Use Responses API with `background=true`** - Not the old completions API

## 🏗️ Architecture Overview (Corrected)

```
Claude Code ──▶ Bash CLI (deep-research)
                 │
                 ▼
           Python Orchestrator
           (responses.create with background=true)
                 │
                 ├─▶ OpenAI API (Deep Research + web_search_preview)
                 │
                 └─▶ Task DB (SQLite WAL or Redis)

Public ingress (pick one):
  A) Tailscale Funnel → Flask/FastAPI Webhook (SDK verify via client.webhooks.unwrap)
  B) Public HTTPS (e.g., Caddy/NGINX) → same webhook app

Webhook app ──▶ queue ──▶ post-processing:
                            • extract final text + citations
                            • persist events/usage
                            • write Obsidian (atomic)
                            • notify (optional)
```

## 📋 Implementation Components

### 1. **Core Python Module** (`deep_research/`)
```
deep_research/
├── __init__.py
├── client.py          # OpenAI API client
├── webhook.py         # Flask webhook server
├── database.py        # SQLite task tracking
├── obsidian.py        # Obsidian formatting & saving
├── queue_worker.py    # Async task processing
└── config.py          # Configuration management
```

### 2. **Bash CLI Wrapper** (`deep-research`)
```bash
# Commands to implement:
deep-research query "Research question"     # Start new research
deep-research status <task-id>             # Check task status
deep-research list [--limit 20]            # List recent tasks
deep-research cancel <task-id>             # Cancel running task
deep-research logs <task-id>               # View task logs
deep-research server start/stop/status     # Manage webhook server
deep-research config                       # Configure settings
```

### 3. **Database Schema** (SQLite WAL Mode)
```sql
-- Enable WAL mode for better concurrency
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

-- Tasks table
tasks (
    id TEXT PRIMARY KEY,              -- OpenAI response ID
    status TEXT,                       -- pending|running|completed|error|cancelled
    model TEXT,                        -- o3-deep-research-2025-06-26 or o4-mini-deep-research-2025-06-26
    query TEXT,                        -- Original research query
    enriched_query TEXT,               -- Enhanced query after preprocessing
    created_at TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    output_file TEXT,                  -- Path to Obsidian file
    error_message TEXT,
    tool_calls_count INTEGER,
    estimated_cost REAL,
    metadata JSON                      -- Additional data
)

-- Webhook events table (raw storage)
webhook_events (
    webhook_id TEXT PRIMARY KEY,       -- event.id or hash(body)
    task_id TEXT REFERENCES tasks(id),
    event_type TEXT,                   -- response.completed|response.failed|response.cancelled
    received_at TIMESTAMP,
    processed_at TIMESTAMP,
    raw_payload TEXT
)

-- Task events table (normalized from webhooks)
task_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id TEXT REFERENCES tasks(id),
    event_type TEXT,                   -- response.completed|response.failed
    status TEXT,                       -- queued|in_progress|completed|failed|cancelled
    occurred_at TIMESTAMP,
    payload_json TEXT
)

-- Citations table (extracted from annotations)
citations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id TEXT REFERENCES tasks(id),
    title TEXT,
    url TEXT,
    start_index INTEGER,
    end_index INTEGER
)

-- Configuration table
config (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP
)

-- Performance indexes
CREATE INDEX IF NOT EXISTS idx_tasks_created ON tasks(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_events_task ON task_events(task_id, occurred_at DESC);
CREATE INDEX IF NOT EXISTS idx_citations_task ON citations(task_id);
```

### 4. **Environment Configuration**
```bash
# .env file structure (chmod 0600)
OPENAI_API_KEY=sk-...
OPENAI_WEBHOOK_SECRET=whsec_...

# Models (use exact IDs from API)
OPENAI_DEFAULT_MODEL=o3-deep-research-2025-06-26
OPENAI_FALLBACK_MODEL=o4-mini-deep-research-2025-06-26

# Responses API behavior
BACKGROUND_MODE=true              # always for Deep Research
MAX_OUTPUT_TOKENS=8000            # cap synthesis length

# Web search tool configuration
WEB_SEARCH_CONTEXT_SIZE=medium    # low|medium|high (affects cost/latency)
WEB_SEARCH_USER_LOCATION_JSON=''  # optional, JSON format

# Cost/rate guards
MAX_TOOL_CALLS=40                 # hard limit per task
DAILY_SPEND_LIMIT_USD=5.00        # daily budget cap
TASK_COST_LIMIT_USD=1.50          # per-task maximum

# Webhook ingress
WEBHOOK_HOST=0.0.0.0
WEBHOOK_PORT=8080
USE_TAILSCALE_FUNNEL=true         # Funnel for public access, not Serve!

# Paths
OBSIDIAN_VAULT_PATH=~/dev/02_Areas/Obsidian
DEEP_RESEARCH_OUTPUT_DIR=00 Inbox/Deep Research
DATABASE_PATH=~/.deep-research/tasks.db
LOG_PATH=~/.deep-research/logs

# Features
ENABLE_QUERY_ENRICHMENT=true      # Use GPT-4 to enhance queries
ENABLE_AUTO_RETRY=true             # Retry failed tasks
WEBHOOK_TIMEOUT_SECONDS=2          # Quick ACK to OpenAI
```

## 🔐 Security Implementation

### Webhook Verification (Using SDK Helpers)
```python
# Correct implementation using OpenAI SDK
from flask import Flask, request
from openai import OpenAI
import hashlib, sqlite3, time

app = Flask(__name__)
client = OpenAI()  # uses OPENAI_WEBHOOK_SECRET from env

def seen_event(db, dedupe_key: str) -> bool:
    with db:
        cur = db.execute("SELECT 1 FROM webhook_events WHERE webhook_id = ?", (dedupe_key,))
        return cur.fetchone() is not None

@app.post("/webhook")
def webhook():
    raw = request.get_data(as_text=True)  # MUST use RAW body
    try:
        # SDK handles all signature verification
        event = client.webhooks.unwrap(raw, request.headers)
    except Exception as e:
        app.logger.warning(f"Invalid signature: {e}")
        return "invalid", 400

    # Idempotency: use event.id or fallback to body hash
    evt_id = getattr(event, "id", None) or hashlib.sha256(raw.encode()).hexdigest()

    db = sqlite3.connect(DB_PATH)
    if seen_event(db, evt_id):
        return "ok", 200  # Already processed, idempotent
    
    with db:
        db.execute(
            "INSERT INTO webhook_events (webhook_id, task_id, event_type, received_at, raw_payload) "
            "VALUES (?, ?, ?, ?, ?)",
            (evt_id, getattr(event, "response_id", None), event.type, int(time.time()), raw)
        )
    
    # Route by event type
    if event.type == "response.completed":
        task_queue.put(event)  # Process async
    elif event.type == "response.failed":
        handle_failure(event)
    
    return "ok", 200  # Quick ACK to OpenAI
```

### Secret Management
- Store in environment variables (never in code)
- Use `.env` file with restricted permissions (600)
- Optionally integrate with system keychain

## 🚀 Deployment Strategy

### Phase 1: Local Development (Week 1)
- [ ] Set up Python environment with dependencies
- [ ] Implement core client and webhook server
- [ ] Basic SQLite database for task tracking
- [ ] Simple Obsidian file saving

### Phase 2: Tailscale Integration (Week 1)
- [ ] Configure Tailscale Funnel for public HTTPS access
- [ ] Test webhook connectivity
- [ ] Implement signature verification
- [ ] Add idempotency handling

### Phase 3: Enhanced Features (Week 2)
- [ ] Query enrichment with GPT-4
- [ ] Progress tracking and cancellation
- [ ] Cost estimation and limits
- [ ] Retry logic for failures

### Phase 4: Production Ready (Week 2)
- [ ] Comprehensive error handling
- [ ] Logging and monitoring
- [ ] Performance optimization
- [ ] Documentation and examples

## 🧪 Testing Strategy

### Unit Tests
- Webhook signature verification
- Database operations
- Obsidian formatting
- Queue processing

### Integration Tests
- End-to-end research flow
- Webhook retry scenarios
- Task cancellation
- Error recovery

### Manual Testing Checklist
- [ ] Simple web search query
- [ ] Complex multi-tool research
- [ ] Task cancellation mid-process
- [ ] Webhook failure and retry
- [ ] Database persistence
- [ ] Obsidian file creation

## 📊 Monitoring & Observability

### Metrics to Track
- Task success/failure rate
- Average completion time
- Tool calls per task
- Estimated costs
- Webhook delivery success rate

### Logging
```python
# Structured logging format
{
    "timestamp": "2025-08-17T10:30:00Z",
    "level": "INFO",
    "component": "webhook_server",
    "task_id": "resp_123",
    "event": "task_completed",
    "duration_seconds": 145,
    "tool_calls": 23
}
```

## 🎨 Obsidian Output Format

### File Structure
```markdown
---
title: Deep Research - [Query Summary]
date: 2025-08-17T10:30:00
task_id: resp_abc123
model: o4-mini-deep-research
status: completed
duration: 2m 25s
tool_calls: 23
estimated_cost: $0.45
tags: [deep-research, ai-generated, web-search]
---

# [Query Title]

## Executive Summary
[Brief overview of findings]

## Key Findings
[Main research results with citations]

## Detailed Analysis
[Full research output]

---

## Research Process

### Web Searches (15)
- Searched: "latest AI developments 2025"
- Opened: https://example.com/ai-news
- Found in page: "transformer architecture improvements"

### Code Execution (3)
- Analyzed data trends
- Generated visualization
- Statistical analysis

### Sources
[All cited sources with links]
```

## 📦 Implementation Code Snippets

### Creating a Research Task (Correct API Usage)
```python
from openai import OpenAI

client = OpenAI()

def start_research(query: str, model: str = "o3-deep-research-2025-06-26", 
                   context_size: str = "medium", max_tool_calls: int = 40):
    """Start a deep research task using Responses API"""
    tools = [{
        "type": "web_search_preview",
        "search_context_size": context_size  # low|medium|high
    }]
    # Optionally add: {"type": "code_interpreter"}
    
    resp = client.responses.create(
        model=model,
        input=[{
            "role": "user",
            "content": [{"type": "input_text", "text": query}]
        }],
        tools=tools,
        reasoning={"summary": "auto"},
        background=True,  # ALWAYS true for Deep Research
        max_output_tokens=int(os.getenv("MAX_OUTPUT_TOKENS", "8000")),
        max_tool_calls=max_tool_calls  # Cost control
    )
    return resp.id  # Store as tasks.id in database
```

### Processing Webhook Events
```python
def process_completed_event(event):
    """Extract and save research results from completed event"""
    # Extract final text (last message)
    final_text = event.output[-1].content[0].text
    
    # Extract citations from annotations
    annotations = event.output[-1].content[0].annotations
    citations = [{
        "title": ann.title,
        "url": ann.url,
        "start_index": ann.start_index,
        "end_index": ann.end_index
    } for ann in annotations]
    
    # Count tool calls by type
    tool_calls = {
        "web_search": 0,
        "code_interpreter": 0
    }
    for item in event.output:
        if item.type == "web_search_call":
            tool_calls["web_search"] += 1
        elif item.type == "code_interpreter_call":
            tool_calls["code_interpreter"] += 1
    
    # Save to database and Obsidian
    save_to_obsidian(event.id, final_text, citations, tool_calls)
```

### CLI with Cost Controls
```bash
# Enhanced CLI usage
deep-research query "Research quantum computing applications" \
  --model o3-deep-research-2025-06-26 \
  --context-size medium \
  --max-tool-calls 30 \
  --cost-cap 1.25 \
  --tags "client:ACME,topic:Q3-planning"

deep-research status resp_abc123  # Shows cost so far
deep-research cancel resp_abc123  # Calls responses.cancel
deep-research logs resp_abc123    # Shows web searches & URLs
```

## 🚦 Success Criteria

### MVP Requirements
- ✅ Can trigger research from Claude Code
- ✅ Receives webhook callbacks via Tailscale Funnel
- ✅ Uses SDK's webhooks.unwrap() for verification
- ✅ Saves results to Obsidian with atomic writes
- ✅ Tracks task status in SQLite WAL database

### Production Requirements
- ✅ Handles failures gracefully with retries
- ✅ Supports task cancellation via responses.cancel
- ✅ Provides accurate cost estimates and caps
- ✅ Includes structured JSON logging with request IDs
- ✅ Secure webhook verification via SDK
- ✅ Idempotent webhook processing with event.id

## 📚 Dependencies

### Python Packages
```txt
openai>=1.50.0       # Deep Research API support (has webhooks.unwrap)
flask>=3.0.0         # Webhook server
python-dotenv        # Environment management
rich                 # CLI formatting
click>=8.0           # CLI framework
jinja2               # Template rendering for Obsidian
# sqlite3 is built-in
```

### System Requirements
- Python 3.10+
- Tailscale installed and configured
- SQLite3
- Bash 4.0+

## 🔄 Next Steps

1. **Validate OpenAI Account Setup**
   - Confirm API access to o3-deep-research-2025-06-26 and o4-mini models
   - Get webhook signing secret from OpenAI dashboard
   - Register webhook URL in OpenAI dashboard (per-project configuration)

2. **Environment Setup**
   ```bash
   cd ~/.scripts/deep-research
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   chmod 0600 .env  # Secure your secrets!
   ```

3. **Tailscale Funnel Configuration (NOT Serve!)**
   ```bash
   tailscale up
   # Use Funnel for public access (required for OpenAI webhooks)
   tailscale funnel 127.0.0.1:8080
   # Copy the https URL for testing
   ```

4. **Start Development**
   - Implement webhook server with `client.webhooks.unwrap()`
   - Test idempotency with duplicate webhook calls
   - Start with o4-mini model for cheaper testing
   - Verify citations extraction from annotations

## 🔍 Key Technical Validations

### Verified Against Current Docs (Aug 2025):
- ✅ Model IDs: `o3-deep-research-2025-06-26` and `o4-mini-deep-research-2025-06-26`
- ✅ Use Responses API with `background=true`, not completions
- ✅ Tailscale Funnel (not Serve) required for public webhooks
- ✅ SDK provides `client.webhooks.unwrap()` for signature verification
- ✅ Web search tool supports `search_context_size` parameter
- ✅ Event types are `response.completed` and `response.failed`

### Cost Considerations:
- Web search with "high" context uses ~3x more tokens than "low"
- Each web_search_call counts as a tool use for billing
- o3 model is ~10x more expensive than o4-mini
- Monitor `max_tool_calls` to prevent runaway costs

## 🤔 Open Questions

1. **Cost Management**: Per-user limits or shared daily budget?
2. **Query Enrichment**: Use GPT-4 preprocessing or trust Deep Research?
3. **Result Caching**: Cache by query hash to avoid duplicate research?
4. **Multi-user**: Need user isolation if sharing the system?
5. **Production Hosting**: Stable Tailscale node or dedicated HTTPS endpoint?

## 🧪 60-Second Smoke Test

Once implementation is ready, validate the entire flow:

1. **Expose webhook publicly (dev):**
   ```bash
   tailscale up
   tailscale funnel 127.0.0.1:8080
   # Copy the Funnel URL (https://<node>.<tailnet>.ts.net)
   ```

2. **Register webhook in OpenAI dashboard:**
   - Navigate to project settings → Webhooks
   - Add the Funnel URL + `/webhook` path
   - Copy the signing secret to `.env`

3. **Start webhook server:**
   ```bash
   python webhook_server.py
   # Verify it passes raw body to client.webhooks.unwrap()
   # Invalid signatures should return 400
   ```

4. **Run test research with cost controls:**
   ```bash
   deep-research query "What is quantum computing?" \
     --model o4-mini-deep-research-2025-06-26 \
     --context-size low \
     --max-tool-calls 10
   ```

5. **Verify complete flow:**
   - ✅ Receive `response.completed` event
   - ✅ Obsidian note created with citations
   - ✅ Tool calls counted and logged
   - ✅ Cost tracking accurate

If you see tool-support errors, verify the model supports `web_search_preview`.

## 📈 Future Enhancements

- **Vector Store Integration**: Connect user's documents via OpenAI vector stores
- **MCP Server Support**: Add compatible MCP servers for private data
- **Research Templates**: Predefined queries for common research patterns
- **Scheduled Research**: Cron-like scheduling for recurring research
- **Research Comparison**: Diff between research runs on same topic
- **Export Formats**: Support JSON, PDF, HTML exports
- **Claude Integration**: Feed research results back into Claude's context