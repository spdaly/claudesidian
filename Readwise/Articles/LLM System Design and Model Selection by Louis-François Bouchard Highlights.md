# LLM System Design and Model Selection

![rw-book-cover](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2019/06/anatomy-1751201_crop-355c0e36608a04c85c14cdb0023bc1e3-1.jpg)
<br>
>[!note]- Readwise Information
>Title:: LLM System Design and Model Selection
>Author:: [[Louis-François Bouchard]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-08-26]]
>Last-Highlighted-Date:: [[2025-08-31]]
>Readwise-Link:: https://readwise.io/bookreview/54664704
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[Large Language Model]] [[System Design]] 
>Source URL:: https://www.oreilly.com/radar/llm-system-design-and-model-selection/
--- 

## Linked Notes
```dataview
LIST
FROM [[LLM System Design and Model Selection by Louis-François Bouchard Highlights]]
```

---

## Highlights
- AI, in one sense, is getting cheaper faster than any previous technology, at least per *unit of intelligence*. For example, input tokens for Gemini Flash Lite 2.5 are approximately 600 times cheaper than what OpenAI’s GPT-3 (Da Vinci 002) cost in August 2022, while outperforming it on every metric. [View Highlight](https://readwise.io/open/932812462) ^rw932812462 
- See also: [[ai economics]] 
- The choices you make in these broader development decisions also decide which LLM and inference settings are optimal for your use case. [View Highlight](https://readwise.io/open/932812560) ^rw932812560
- Pre-training data quality has become just as important as quantity, with better filtering and AI-generated synthetic data contributing to stronger models. [View Highlight](https://readwise.io/open/932814224) ^rw932814224
- Architectural efficiency, like the innovations introduced by Deepseek, has started to close the gap between size and capability. [View Highlight](https://readwise.io/open/932814247) ^rw932814247
- And post-training techniques, especially instruction tuning and reinforcement learning from human or AI feedback (RLHF/RLAIF), have made models more aligned, controllable, and responsive in practice. [View Highlight](https://readwise.io/open/932814316) ^rw932814316
- models like OpenAI’s o1, we’ve entered a new phase where models can trade compute for reasoning *on demand*. Rather than relying solely on what was baked in during training, they can now “think harder” at runtime, running more internal steps, exploring alternative answers, or chaining thoughts before responding. [View Highlight](https://readwise.io/open/932814345) ^rw932814345
- Inference-time compute scaling has introduced a new dynamic in LLM system design: we’ve gone from a single lever, model size, to at least four distinct ways to trade cost for capability at runtime. [View Highlight](https://readwise.io/open/932814356) ^rw932814356 
- See also: [[ai economics]] 
- As these agents Think, Plan, Act, Reassess, Plan, Act, and so on, they often make many LLM steps in a loop, each incurring additional cost. [View Highlight](https://readwise.io/open/932830583) ^rw932830583
- Taken together, these four factors represent a fundamental shift in how model cost scales. For developers designing systems for high-value problems, **10,000x to 1,000,000x differences in API costs to solve a problem based on architectural choices are now realistic possibilities.** [View Highlight](https://readwise.io/open/932830621) ^rw932830621 
- See also: [[ai economics]] [[architecture]] 
- Note: LM solution architects need to take an account the types of API‘s and how LLMs use tokens and how drastically different they can be from model to model
- This shift changes how we think about selection. Choosing an LLM is no longer about chasing the highest benchmark score. It’s about finding the balance point where capability, latency, and cost align with your use case. [View Highlight](https://readwise.io/open/932830670) ^rw932830670 
- See also: [[artificial intelligence]] [[ai economics]] [[architecture]] 
- These benchmarks are a useful starting point, but some models are tuned on benchmark data and real world performance on tasks actually relevant to you will often vary. Filtering benchmark tests and scores by your industry and task category is a valuable step here. An LLM optimized for software development might perform poorly in creative writing or vice versa. The match between a model’s training focus and your application domain can outweigh general-purpose benchmarks. [View Highlight](https://readwise.io/open/932830737) ^rw932830737 
- See also: [[artificial intelligence]] [[architecture]] 
- Note: Ensure you know the source of what the benchmark tests are because they very wildly from benchmark to benchmark
- The rise of increasingly competitive open-weight LLMs, such as Meta’s Llama series, Mistral, Deepseek, Gemma Qwen, and now OpenAI’s GPT-OSS has added a critical dimension to the model selection landscape. [View Highlight](https://readwise.io/open/932831149) ^rw932831149
- This brings us back to the pros and cons of open weights. While Closed API LLMs still lead at the frontier of capability, the primary advantage of open weights models is quick and affordable local testing, unparalleled flexibility, and increased data security when run internally. [View Highlight](https://readwise.io/open/932831171) ^rw932831171
- This often means that using a closed-source API can be cheaper per inference than self-hosting an open model. [View Highlight](https://readwise.io/open/932831211) ^rw932831211
- A Practical Guide to Designing an LLM System [View Highlight](https://readwise.io/open/932831414) ^rw932831414 
- See also: [[architecture]] [[artificial intelligence]] 
