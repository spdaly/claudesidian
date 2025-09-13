---
name: init-bootstrap
description: Interactive setup wizard that helps new users create a personalized CLAUDE.md file based on their Obsidian workflow preferences
allowed-tools: [Read, Write, MultiEdit, Bash]
argument-hint: "(optional) path to existing vault or 'new' for fresh setup"
---

# Initialize Bootstrap Configuration

This command helps you create a personalized CLAUDE.md configuration file by asking questions about your Obsidian workflow and preferences.

## Task

Read the CLAUDE-BOOTSTRAP.md template and interactively gather information about the user's:
- Existing vault structure (if any)
- Workflow preferences
- Note-taking style
- Organization methods
- Specific requirements

Then generate a customized CLAUDE.md file tailored to their needs.

## Process

1. **Check Setup Status**
   - Look for existing CLAUDE.md
   - If exists, ask if they want to update or start fresh
   - Check for CLAUDE-BOOTSTRAP.md template

2. **Gather Vault Information**
   - Ask if they have an existing vault or starting new
   - If existing, explore current folder structure
   - Document any custom organization patterns

3. **Ask Configuration Questions**
   - "Do you follow the PARA method or have a different organization system?"
   - "What are your main use cases? (research, writing, project management, knowledge base, daily notes)"
   - "Do you use any specific plugins or tools with Obsidian?"
   - "What's your preferred naming convention for files?"
   - "Do you work with attachments frequently? (images, PDFs, etc.)"
   - "Do you use git for version control?"
   - "Any specific websites or resources you reference often?"
   - "Do you have any specific writing style preferences?"
   - "Are there any workflows or patterns you want Claude to follow?"

4. **Generate Custom Configuration**
   - Start with CLAUDE-BOOTSTRAP.md as base
   - Add user-specific sections:
     - Custom folder structure
     - Personal workflows
     - Preferred tools and scripts
     - Specific guidelines
   - Include their websites/resources if provided
   - Add any custom naming conventions

5. **Create Supporting Files**
   - Generate initial folder structure if new vault
   - Create README files for main folders
   - Set up .gitignore if using git
   - Create initial templates if requested

6. **Provide Next Steps**
   - Summary of what was created
   - Quick start guide specific to their setup
   - Suggestions for first tasks
   - How to modify configuration later

## Example Output

```markdown
# Your Obsidian Vault Configuration

Generated on: [Date]
Based on your preferences for: [main use cases]

## Your Custom Folder Structure

[Their specific structure with explanations]

## Your Workflows

### Daily Routine
[Based on their answers]

### Project Management
[Their specific approach]

## Your Preferences

### File Naming
- Pattern: [their convention]
- Examples: [specific examples]

### Tools & Scripts
[Relevant scripts for their workflow]

## Quick Start

1. [Personalized first step]
2. [Next action based on their goals]
3. [Specific to their workflow]
```

## Interactive Example

```
User: claude run init-bootstrap
Assistant: Welcome! I'll help you set up your personalized Obsidian + Claude configuration.

First, let me check your current setup...
[Checks for existing files]

I see you're starting fresh! Let me ask you a few questions to customize your setup:

1. **What will you primarily use this vault for?**
   (research, writing, project management, daily notes, knowledge base, or combination?)

User: I'll use it for research and writing, plus managing client projects