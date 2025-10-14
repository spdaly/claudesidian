# Planning Is a Key Agenti...

![rw-book-cover](https://pbs.twimg.com/profile_images/733174243714682880/oyG30NEH.jpg)
<br>
>[!note]- Readwise Information
>Title:: Planning Is a Key Agenti...
>Author:: [[@AndrewYNg on Twitter]]
>Type:: #Readwise/category/tweets
>Published-Date:: [[2024-04-14]]
>Last-Highlighted-Date:: [[2024-04-15]]
>Readwise-Link:: https://readwise.io/bookreview/39662476
>Readwise-Source:: #Readwise/source/twitter
>Source URL:: https://twitter.com/AndrewYNg/status/1779606380665803144
--- 

## Linked Notes
```dataview
LIST
FROM [[Planning Is a Key Agenti... by @AndrewYNg on Twitter Highlights]]
```

---

## Highlights
- Planning is a key agentic AI design pattern in which we use a large language model (LLM) to autonomously decide on what sequence of steps to execute to accomplish a larger task. For example, if we ask an agent to do online research on a given topic, we might use an LLM to break down the objective into smaller subtasks, such as researching specific subtopics, synthesizing findings, and compiling a report.
  Many people had a “ChatGPT moment” shortly after ChatGPT was released, when they played with it and were surprised that it significantly exceeded their expectation of what AI can do. If you have not yet had a similar “AI Agentic moment,” I hope you will soon. I had one several months ago, when I presented a live demo of a research agent I had implemented that had access to various online search tools.
  I had tested this agent multiple times privately, during which it consistently used a web search tool to gather information and wrote up a summary. During the live demo, though, the web search API unexpectedly returned with a rate limiting error. I thought my demo was about to fail publicly, and I dreaded what was to come next. To my surprise, the agent pivoted deftly to a Wikipedia search tool — which I had forgotten I’d given it — and completed the task using Wikipedia instead of web search.
  This was an AI Agentic moment of surprise for me. I think many people who haven’t experienced such a moment yet will do so in the coming months. It’s a beautiful thing when you see an agent autonomously decide to do things in ways that you had not anticipated, and succeed as a result!
  Many tasks can’t be done in a single step or with a single tool invocation, but an agent can decide what steps to take. For example, to simplify an example from the HuggingGPT paper (cited below), if you want an agent to consider a picture of a boy and draw a picture of a girl in the same pose, the task might be decomposed into two distinct steps: (i) detect the pose in the picture of the boy and (ii) render a picture of a girl in the detected pose. An LLM might be fine-tuned or prompted (with few-shot prompting) to specify a plan by outputting a string like "{tool: pose-detection, input: image.jpg, output: temp1 } {tool: pose-to-image, input: temp1, output: final.jpg}".
  This structured output, which specifies two steps to take, then triggers software to invoke a pose detection tool followed by a pose-to-image tool to complete the task. (This example is for illustrative purposes only; HuggingGPT uses a different format.)
  Admittedly, many agentic workflows do not need planning. For example, you might have an agent reflect on, and improve, its output a fixed number of times. In this case, the sequence of steps the agent takes is fixed and deterministic. But for complex tasks in which you aren’t able to specify a decomposition of the task into a set of steps ahead of time, Planning allows the agent to decide dynamically what steps to take.
  On one hand, Planning is a very powerful capability; on the other, it leads to less predictable results. In my experience, while I can get the agentic design patterns of Reflection and Tool use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do. But the field continues to evolve rapidly, and I'm confident that Planning abilities will improve quickly.
  If you’re interested in learning more about Planning with LLMs, I recommend:
  - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, Wei et al. (2022)
  - HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face, Shen et al. (2023)
  - Understanding the planning of LLM agents: A survey, by Huang et al. (2024)
  [Original text: https://t.co/pWmIR9wEki ] [View Tweet](https://readwise.io/open/707217334) ^rw707217334
