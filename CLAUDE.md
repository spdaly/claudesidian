# Claude Code + Obsidian Guidelines

**A starter kit for using Claude Code as your second brain**

## Quick Start

This is a template vault designed to work seamlessly with Claude Code. It follows the PARA method and includes helpful scripts and structures to maximize your AI-assisted thinking and note-taking.

## Core Principles

### 1. Thinking Mode vs Writing Mode
When working with Claude Code, be explicit about your intent:
- **Thinking mode**: "I'm in thinking mode, not writing mode. Ask me questions and help me explore ideas."
- **Writing mode**: "Now I'm ready to write. Help me create the artifact."

### 2. Everything is Local
- All notes are markdown files in folders
- Sync with Git for version control
- Claude Code can read, write, and organize everything

### 3. Use the PARA Method
- **Projects (01)**: Time-bound initiatives with clear completion criteria
- **Areas (02)**: Ongoing responsibilities without end dates  
- **Resources (03)**: Reference materials by topic
- **Archive (04)**: Completed or inactive items
- **Inbox (00)**: Temporary capture point

## Essential Commands

### Git Workflow
```bash
git pull                  # Start each session
git add .                 # After creating/editing
git commit -m "message"   # Save your work
git push                  # Sync to remote
```

### Helper Scripts (via npm/pnpm)
- `pnpm attachments:list` - List unprocessed attachments
- `pnpm attachments:organized` - Count organized files
- `pnpm attachments:update-links` - Update links after moving files

## Working with Claude Code

### Starting a New Project
1. Create a folder in `01_Projects/[Project Name]`
2. Start Claude Code in the vault root directory
3. Tell it: "I'm working on [project] in thinking mode"
4. Let it search your existing notes for relevant content

### Research Workflow
1. Create subfolders:
   - `Research/` - Articles and source materials
   - `Chats/` - Saved AI conversations
   - `Daily Progress/` - Running log of insights
2. Use Claude Code to synthesize across sources
3. Ask: "Catch me up on the last few days of research"

### Best Practices
- **Be a token maximalist**: Provide lots of context
- **Don't trust, verify**: Always read AI-generated content
- **Iterate freely**: Use chat to refine, not perfect prompts
- **Save everything**: Capture chats, ideas, fragments

## Key Reminders

### When AI Tries to Write Too Soon
Add to your instructions:
```
CRITICAL: When I say I'm "just collecting source materials" or "I'm in thinking mode", take this LITERALLY. Do NOT create outlines, drafts, or any versions of talks/writing. Only gather and organize the requested materials.
```

### File Organization
- Keep numbered files (00, 01, etc.) in Inbox permanently
- Process other Inbox items weekly
- Move completed projects to Archive with summaries
- Use descriptive filenames with dates (YYYY-MM-DD)

## Advanced Setup

### Mobile Access with Claude Code
1. Set up a mini PC or cloud server
2. Install Tailscale for VPN access
3. Use Termius app to connect
4. Run Claude Code from anywhere

### Creating Custom Agents
Create specialized agents for different modes:
- Thinking partner (asks questions, tracks insights)
- Research assistant (finds and synthesizes)
- Editor (reviews and improves)

## Folder Structure

```
claudesidian/
├── 00_Inbox/           # Capture and process
├── 01_Projects/        # Active work
├── 02_Areas/           # Ongoing responsibilities  
├── 03_Resources/       # Reference materials
├── 04_Archive/         # Completed items
├── 05_Attachments/     # Images, PDFs, etc.
├── 06_Metadata/        # Vault documentation
│   ├── Reference/      # Guides and docs
│   └── Templates/      # Reusable structures
├── .scripts/           # Helper scripts
├── package.json        # Script definitions
└── CLAUDE.md          # This file
```

## Getting Started Checklist

- [ ] Clone this repository
- [ ] Open in Obsidian (optional but recommended)
- [ ] Start Claude Code in the vault directory
- [ ] Create your first project folder
- [ ] Try the "thinking mode" approach
- [ ] Set up Git for syncing (optional)
- [ ] Customize folder structure as needed

## Tips from Experience

1. **The bicycle analogy**: It feels weird at first, then becomes natural
2. **Read more than write**: AI's superpower is synthesis, not generation
3. **Break your flow intentionally**: AI helps you pick up where you left off
4. **Think in projects**: Even casual research benefits from structure
5. **Embrace the chaos**: Let AI handle the organization while you think

## Questions or Ideas?

This is a living document. As you develop your own workflows, add them here. The best practices emerge from actual use, not theory.

Remember: The goal isn't to optimize for AI, it's to amplify your own thinking.