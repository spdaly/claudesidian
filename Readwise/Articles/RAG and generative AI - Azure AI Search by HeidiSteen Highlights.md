# RAG and generative AI - Azure AI Search

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
<br>
>[!note]- Readwise Information
>Title:: RAG and generative AI - Azure AI Search
>Author:: [[HeidiSteen]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-09-13]]
>Last-Highlighted-Date:: [[2024-12-04]]
>Readwise-Link:: https://readwise.io/bookreview/46493996
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[retrieval augmented generation]] 
>Source URL:: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
--- 

## Linked Notes
```dataview
LIST
FROM [[RAG and generative AI - Azure AI Search by HeidiSteen Highlights]]
```

---

## Highlights
- • App UX (web app) for the user experience
  • App server or orchestrator (integration and coordination layer)
  • Azure AI Search (information retrieval system)
  • Azure OpenAI (LLM for generative AI) [View Highlight](https://readwise.io/open/820324667) ^rw820324667
- The web app provides the user experience, providing the presentation, context, and user interaction. Questions or prompts from a user start here. Inputs pass through the integration layer, going first to information retrieval to get the search results, but also go to the LLM to set the context and intent.
  The app server or orchestrator is the integration code that coordinates the handoffs between information retrieval and the LLM. Common solutions include [LangChain](https://python.langchain.com/docs/get_started/introduction) to coordinate the workflow. LangChain [integrates with Azure AI Search](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/), making it easier to include Azure AI Search as a [retriever](https://python.langchain.com/docs/how_to/`#`retrievers) in your workflow. [LlamaIndex](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/vector_stores/llama-index-vector-stores-azureaisearch) and [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/announcing-semantic-kernel-integration-with-azure-cognitive-search/) are other options.
  The information retrieval system provides the searchable index, query logic, and the payload (query response). The search index can contain vectors or nonvector content. Although most samples and demos include vector fields, it's not a requirement. The query is executed using the existing search engine in Azure AI Search, which can handle keyword (or term) and vector queries. The index is created in advance, based on a schema you define, and loaded with your content that's sourced from files, databases, or storage.
  The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might be a back and forth conversation. If you're using Davinci, the prompt might be a fully composed answer. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service. [View Highlight](https://readwise.io/open/820324308) ^rw820324308
