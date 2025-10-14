# Mistral Living Large, Google's Open Source Challenger, Robot Chemist, Schooling Language Models in Math

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
<br>
>[!note]- Readwise Information
>Title:: Mistral Living Large, Google's Open Source Challenger, Robot Chemist, Schooling Language Models in Math
>Author:: [[The Batch @ DeepLearning.AI]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-03-06]]
>Last-Highlighted-Date:: [[2024-03-06]]
>Readwise-Link:: https://readwise.io/bookreview/38434081
>Readwise-Source:: #Readwise/source/reader
--- 

## Linked Notes
```dataview
LIST
FROM [[Mistral Living Large, Google's Open Source Challenger, Robot Chemist, Schooling Language Models in Math by The Batch @ DeepLearning.AI Highlights]]
```

---

## Highlights
- Progress on LLM-based agents that can autonomously plan out and execute sequences of actions has been rapid, and I continue to see month-over-month improvements. Many projects attempt to take a task like “write a report on topic X” and autonomously take actions such as browsing the web to gather information to synthesize a report. [View Highlight](https://readwise.io/open/689047209) ^rw689047209 
- See also: [[👻 ai highlighted]] 
- Note: What are LLM-based agents and why are they important?
  LLM-based agents are agents that can autonomously plan out and execute sequences of actions. They are important because they can take on tasks such as browsing the web to gather information to synthesize a report.
  What is the benefit of Mistral AI's partnership with Microsoft?
  The partnership between Mistral AI and Microsoft gives the startup crucial processing power for training large models and greater access to potential customers around the world. It gives the tech giant greater access to the European market. And it gives Azure customers access to a high-performance model that’s tailored to Europe’s unique regulatory environment.
  What is the significance of Gemma, Google's 8.5 billion-parameter large language model?
  Gemma raises the bar for models of roughly 7 billion parameters. It delivers exceptional performance in a relatively small parameter counts, expanding the options for developers who are building on top of LLMs.
  1. What are the potential benefits and drawbacks of multi-agent systems in AI architecture?
  2. How does Mistral AI's partnership with Microsoft impact the European AI industry and regulatory environment?
  3. In what ways can RoboChem's integrated robotic system improve lab productivity and reduce costs?
- So far, I see agents that browse the web progressing much faster because the cost of experimentation is low, and this is key to rapid technical progress. It’s cheap to fetch a webpage, and if your agent chooses poorly and reads the wrong page, there’s little harm done. In comparison, sending a product or moving a physical robot are costly actions, which makes it hard to experiment rapidly. Similarly, agents that generate code (that you can run in a sandbox environment) are relatively cheap to run, leading to rapid experimentation and progress. [View Highlight](https://readwise.io/open/689047161) ^rw689047161 
- See also: [[👻 ai highlighted]] 
- Although today’s research agents, whose tasks are mainly to gather and synthesize information, are still in an early phase of development, I expect to see rapid improvements. ChatGPT, Bing Chat, and Gemini can already browse the web, but their online research tends to be limited; this helps them get back to users quickly. But I look forward to the next generation of agents that can spend minutes or perhaps hours doing deep research before getting back to you with an output. Such algorithms will be able to generate much better answers than models that fetch only one or two pages before returning an answer. [View Highlight](https://readwise.io/open/689047201) ^rw689047201 
- See also: [[👻 ai highlighted]] 
- Another common design pattern is to have one agent write and a second agent work as a critic to give constructive feedback to the first agent to help it improve. This can result in much higher-quality output. Open-source frameworks like Microsoft’s [AutoGen](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VWH5dC7Ct8F8W4v9jh17YmkDcW37H_hZ5blsqsN8rPF5s3qgyTW7lCdLW6lZ3lpW7rzr_T2ky2R-W44rcBB8K9dkcW5LM6N32g4DRdW8Fl4xf6CNWGlW5hCQxB1bLssNN7J5-_dHsVNdW7lbjHR9hp96gN6BXgN0P3YDJW15GfYp1w_qgwW2jXpq74fY9ZkN22k3nSRD1-xW8vPxNX1JmCqFN30lFgDY39XxW8K6HFs8qhRW9W8l2k842DjxjZW5bPhqL57jQHlN579lK57g7KFW8VntQh507c22W4wzkt893md17W5xMjPF7VpgzfW7pZ8gK3sGp4RW50jq5G6y2b1ZW7nlp1W4Z2WBVW7QSM5-2TzDh-f2Mwdz-04), [Crew AI](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VWH5dC7Ct8F8W4v9jh17YmkDcW37H_hZ5blsqsN8rPF4T3qgyTW69sMD-6lZ3l_N48GHCsSZpk7W1sSVWz4r14ZnVLX_lq3jJyjVW7rRbx69l8NbnW52vTjY4rcpTqW8YJyxM2pcKsVW4cjHQh5K-2pdW9dz7Vd7-msGHVWPtwl2X0-h2W8M01ZY69jVN5W70QdQK7Rf8VtN61nsFDX7k6gW7S5t_K23ly29VfpdGC5XXJc6W590TQJ292D_fW3-Gp1l8c8H85W1GdZBk3vZM4KW2_mKVJ1ZbvjpW88f7Gf1ng3D8W5slWxB5gvQZdf1lNXGF04), and [LangGraph](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VWH5dC7Ct8F8W4v9jh17YmkDcW37H_hZ5blsqsN8rPF5s3qgyTW7lCdLW6lZ3kFW1VPVpq2mPyTbW7_clm76W8_v2W47zgLN7PhKYYW6J3WKT60PHHTN3JMV7QmH69BW7J0j2W56WgWWN3X-K0Sjm0fWW63_xll41sbRnW2Pc06_4S8MZCW67Zn993VfCK8W9ghB_Y2H1P2LW2mC2QG827ZNkW1KVd-f2C_RR_W4jrL6G3QlrK3W7ch66Y2Bz2JLW8CZHSD16zqzGW99Vl8r5LtG1NV89qYg4grX6BW7M1Ws32xLbcbW638lfl5Nw1yzW3XH5Y66NDxLMW8CMcN67lwQSjW49Wj2w7d2Rh1W1wkftJ7VKlMPf44TpkK04) are making it easier for developers to program multiple agents that collaborate to get a task done. [View Highlight](https://readwise.io/open/689047158) ^rw689047158 
- See also: [[👻 ai highlighted]] 
- Why it matters: The partnership between Mistral AI and Microsoft gives the startup crucial processing power for training large models and greater access to potential customers around the world. It gives the tech giant greater access to the European market. And it gives Azure customers access to a high-performance model that’s tailored to Europe’s unique regulatory environment. [View Highlight](https://readwise.io/open/689047163) ^rw689047163 
- See also: [[👻 ai highlighted]] 
- Behind the news: Google has a rich history of open source AI projects including AlphaFold, TensorFlow, several versions of BERT and T5, and the massive Switch. Lately, though, its open source efforts have been overshadowed by open large language models (LLMs) from Meta, Microsoft, and Mistral.ai. LLMs small enough to run on a laptop have opened open source AI to an expanding audience of developers. [View Highlight](https://readwise.io/open/689047198) ^rw689047198 
- See also: [[👻 ai highlighted]] 
- Why it matters: Gemma raises the bar for models of roughly 7 billion parameters. It delivers exceptional performance in a relatively small parameter counts, expanding the options for developers who are building on top of LLMs. [View Highlight](https://readwise.io/open/689047155) ^rw689047155 
- See also: [[👻 ai highlighted]] 
- A similar technique exists for division. Together, these approaches can enable LLMs to perform more complicated mathematical tasks. [View Highlight](https://readwise.io/open/689047195) ^rw689047195 
- See also: [[👻 ai highlighted]] 
