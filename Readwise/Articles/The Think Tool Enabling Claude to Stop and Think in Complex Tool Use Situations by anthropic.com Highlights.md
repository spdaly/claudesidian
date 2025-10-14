# The "Think" Tool: Enabling Claude to Stop and Think in Complex Tool Use Situations

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/84a488382e0428a5eebade574af047e5d3b610ab-2400x1260.png)
<br>
>[!note]- Readwise Information
>Title:: The "Think" Tool: Enabling Claude to Stop and Think in Complex Tool Use Situations
>Author:: [[anthropic.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-03-21]]
>Last-Highlighted-Date:: [[2025-08-31]]
>Readwise-Link:: https://readwise.io/bookreview/54666733
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Artificial Intelligence]] [[Claude]] [[Prompt Engineering]] [[Reasoning]] 
>Source URL:: https://www.anthropic.com/engineering/claude-think-tool
--- 

## Linked Notes
```dataview
LIST
FROM [[The "Think" Tool: Enabling Claude to Stop and Think in Complex Tool Use Situations by anthropic.com Highlights]]
```

---

## Highlights
- The "think" tool is for Claude, once it starts generating a response, to add a step to stop and think about whether it has all the information it needs to move forward. This is particularly helpful when performing long chains of tool calls or in long multi-step conversations with the user. [View Highlight](https://readwise.io/open/932831953) ^rw932831953
- The “think” tool is better suited for when Claude needs to call complex tools, analyze tool outputs carefully in long chains of tool calls, navigate policy-heavy environments with detailed guidelines, or make sequential decisions where each step builds on previous ones and mistakes are costly. [View Highlight](https://readwise.io/open/932832100) ^rw932832100
- The combination of the "think" tool with optimized prompting delivered the strongest performance by a significant margin, likely due to the high complexity of the [airline policy](https://github.com/sierra-research/tau-bench/blob/main/tau_bench/envs/airline/wiki.md) part of the benchmark, where the model benefitted the most from being given examples of how to “think.” [View Highlight](https://readwise.io/open/932832272) ^rw932832272
