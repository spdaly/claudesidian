# How We Built Our Multi-Agent Research System

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/5cf046fff69b847bfa78c12723dd466b285c0218-2400x1260.png)
<br>
>[!note]- Readwise Information
>Title:: How We Built Our Multi-Agent Research System
>Author:: [[anthropic.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-06-13]]
>Last-Highlighted-Date:: [[2025-08-31]]
>Readwise-Link:: https://readwise.io/bookreview/54666791
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Agents]] [[Artificial Intelligence]] [[Claude]] 
>Source URL:: https://www.anthropic.com/engineering/built-multi-agent-research-system
--- 

## Linked Notes
```dataview
LIST
FROM [[How We Built Our Multi-Agent Research System by anthropic.com Highlights]]
```

---

## Highlights
- Research work involves open-ended problems where it’s very difficult to predict the required steps in advance. You can’t hardcode a fixed path for exploring complex topics, as the process is inherently dynamic and path-dependent. When people conduct research, they tend to continuously update their approach based on discoveries, following leads that emerge during investigation. [View Highlight](https://readwise.io/open/932832832) ^rw932832832
- The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent. Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations. [View Highlight](https://readwise.io/open/932832863) ^rw932832863
- Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. [View Highlight](https://readwise.io/open/932832897) ^rw932832897
- **Debugging benefits from new approaches.** Agents make dynamic decisions and are non-deterministic between runs, even with identical prompts. This makes debugging harder. [View Highlight](https://readwise.io/open/932833712) ^rw932833712
