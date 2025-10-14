# Effective Context Engineering for AI Agents

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/ea2bf01aa874d7ab776453e97dfeed5d2bf5a116-2400x1260.png)
<br>
>[!note]- Readwise Information
>Title:: Effective Context Engineering for AI Agents
>Author:: [[anthropic.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2025-09-29]]
>Last-Highlighted-Date:: [[2025-10-07]]
>Readwise-Link:: https://readwise.io/bookreview/55457094
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[ai]] [[context engineering]] 
>Source URL:: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
--- 

## Linked Notes
```dataview
LIST
FROM [[Effective Context Engineering for AI Agents by anthropic.com Highlights]]
```

---

## Highlights
- “what configuration of context is most likely to generate our model’s desired behavior?" [View Highlight](https://readwise.io/open/945242692) ^rw945242692
- **Context** refers to the set of tokens included when sampling from a large-language model (LLM). [View Highlight](https://readwise.io/open/945242700) ^rw945242700
- The **engineering** problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome. [View Highlight](https://readwise.io/open/945242722) ^rw945242722
- **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts. [View Highlight](https://readwise.io/open/945242745) ^rw945242745
- Context, therefore, must be treated as a finite resource with diminishing marginal returns. [View Highlight](https://readwise.io/open/945439861) ^rw945439861
- As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus. [View Highlight](https://readwise.io/open/945439888) ^rw945439888
- **System prompts** should be extremely clear and use simple, direct language that presents ideas at the *right altitude* for the agent. [View Highlight](https://readwise.io/open/945440610) ^rw945440610
- we recommend working to curate a set of diverse, canonical examples that effectively portray the expected behavior of the agent. [View Highlight](https://readwise.io/open/945440689) ^rw945440689
- Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt—it's thoughtfully curating what information enters the model's limited attention budget at each step. [View Highlight](https://readwise.io/open/945441160) ^rw945441160
