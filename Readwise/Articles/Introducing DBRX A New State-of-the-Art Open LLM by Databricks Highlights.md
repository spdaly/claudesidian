# Introducing DBRX: A New State-of-the-Art Open LLM

![rw-book-cover](https://www.databricks.com/sites/default/files/2024-03/dbrx-technical-blog-og_0.png)
<br>
>[!note]- Readwise Information
>Title:: Introducing DBRX: A New State-of-the-Art Open LLM
>Author:: [[Databricks]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-03-27]]
>Last-Highlighted-Date:: [[2024-03-28]]
>Readwise-Link:: https://readwise.io/bookreview/39093928
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm
--- 

## Linked Notes
```dataview
LIST
FROM [[Introducing DBRX: A New State-of-the-Art Open LLM by Databricks Highlights]]
```

---

## Highlights
- Today, we are excited to introduce DBRX, an open, general-purpose LLM created by Databricks. Across a range of standard benchmarks, DBRX sets a new state-of-the-art for established open LLMs. Moreover, it provides the open community and enterprises building their own LLMs with capabilities that were previously limited to closed model APIs; according to our measurements, it surpasses GPT-3.5, and it is competitive with Gemini 1.0 Pro. It is an especially capable code model, surpassing specialized models like CodeLLaMA-70B on programming, in addition to its strength as a general-purpose LLM. [View Highlight](https://readwise.io/open/698957447) ^rw698957447 
- See also: [[👻 ai highlighted]] 
- mixture-of-experts [View Highlight](https://readwise.io/open/698957494) ^rw698957494
- **Programming and mathematics.** DBRX Instruct is especially strong at programming and mathematics. It scores higher than the other open models we evaluated on HumanEval (70.1% vs. 63.2% for Grok-1, 54.8% for Mixtral Instruct, and 32.2% for the best-performing LLaMA2-70B variant) and GSM8k (66.9% vs. 62.9% for Grok-1, 61.1% for Mixtral Instruct, and 54.1% for the best-performing LLaMA2-70B variant). [View Highlight](https://readwise.io/open/698957444) ^rw698957444 
- See also: [[👻 ai highlighted]] 
- **MMLU.** DBRX Instruct scores higher than all other models we consider on MMLU, reaching 73.7%. [View Highlight](https://readwise.io/open/698957445) ^rw698957445 
- See also: [[👻 ai highlighted]] 
- We processed and cleaned this data using Apache Spark™ and Databricks notebooks. We trained DBRX using optimized versions of our open-source training libraries: [MegaBlocks](https://github.com/stanford-futuredata/megablocks), [LLM Foundry](https://github.com/mosaicml/llm-foundry), [Composer](https://github.com/mosaicml/composer), and [Streaming](https://github.com/mosaicml/streaming). We managed large scale model training and finetuning across thousands of GPUs using our Mosaic AI Training service. We logged our results using [MLflow](https://mlflow.org/). [View Highlight](https://readwise.io/open/698957450) ^rw698957450 
- See also: [[👻 ai highlighted]] 
- At Databricks, we believe that every enterprise should have the ability to control its data and its destiny in the emerging world of GenAI. DBRX is a central pillar of our next generation of GenAI products, and we look forward to the exciting journey that awaits our customers as they leverage the capabilities of DBRX and the tools we used to build it. In the past year, we have trained thousands of LLMs with our customers. DBRX is only one example of the powerful and efficient models being built at Databricks for a wide range of applications, from internal features to ambitious use-cases for our customers. [View Highlight](https://readwise.io/open/698957448) ^rw698957448 
- See also: [[👻 ai highlighted]] 
