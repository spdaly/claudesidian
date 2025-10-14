# An Introduction to RAG and Simple/ Complex RAG

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/0WYv0_CaBmCTt7FXc)
<br>
>[!note]- Readwise Information
>Title:: An Introduction to RAG and Simple/ Complex RAG
>Author:: [[Chia Jeng Yang]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-12-08]]
>Last-Highlighted-Date:: [[2024-01-02]]
>Readwise-Link:: https://readwise.io/bookreview/36129927
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[artificial intelligence]] [[retrieval augmented generation]] 
>Source URL:: https://medium.com/enterprise-rag/an-introduction-to-rag-and-simple-complex-rag-9c3aa9bd017b
--- 

## Linked Notes
```dataview
LIST
FROM [[An Introduction to RAG and Simple/ Complex RAG by Chia Jeng Yang Highlights]]
```

---

## Highlights
- RAG is the [biggest business use-case of LLMs](https://x.com/bindureddy/status/1731846525872206216?s=20), and it will be increasingly important to understand RAG, its processes, applicability to your organization, and surrounding tooling [View Highlight](https://readwise.io/open/652672422) ^rw652672422
- In 2023, the use of LLMs saw significant growth in enterprise applications, particularly in the domain of RAG & information retrieval. According to the [2023 Retool Report](https://retool.com/reports/state-of-ai-2023), an impressive 36.2% of enterprise LLM use cases now employ RAG technology. RAG brings the power of LLMs to structured and unstructured data, making enterprise information retrieval more effective and efficient than ever. [View Highlight](https://readwise.io/open/652672442) ^rw652672442
- A typical RAG process, as pictured below, has an LLM, a collection of enterprise documents, and supporting infrastructure to improve information retrieval and answer construction. The RAG pipeline looks at the database for concepts and data that seem similar to the question being asked, extracts the data from a vector database and reformulates the data into an answer that is tailored to the question asked. This makes RAG a powerful tool for companies looking to harness their existing data repositories for enhanced decision-making and information access. [View Highlight](https://readwise.io/open/652672482) ^rw652672482
- The two competing solutions for “talking to your data” with LLMs are RAG and fine-tuning a LLM model. You may typically want to employ a mixture of both, though there may be a resource trade-off consideration. [View Highlight](https://readwise.io/open/652673629) ^rw652673629
- When you fine-tune a model, you re-train a pre-existing black-box LLM using your company data and tweak model configuration to meet the needs of your use case. [View Highlight](https://readwise.io/open/652673871) ^rw652673871
- RAG, on the other hand, retrieves data from externally-stored company documents and supplies it to the black-box LLM to guide response generation. [View Highlight](https://readwise.io/open/652674144) ^rw652674144
- Fine-tuning is a lengthy, costly process, and it is not a good solution for working with company documents/facts that frequently change. [View Highlight](https://readwise.io/open/652674230) ^rw652674230
- fine-tuned models are very good at recognizing and responding to subtle nuances in tone and content generation [View Highlight](https://readwise.io/open/652674244) ^rw652674244
- fine-tuning is for form, not facts. [View Highlight](https://readwise.io/open/652674272) ^rw652674272
- there are some industries and workflows where the information for answers are structurally written and stored separately. [View Highlight](https://readwise.io/open/652803842) ^rw652803842
- what may initially appear to be simple questions may in fact require multi-hop reasoning. [View Highlight](https://readwise.io/open/652803845) ^rw652803845
- and something that gets missed in academic settings, is the range of poorly formed questions that are asked in practical scenarios, even by sophisticated company leaders [View Highlight](https://readwise.io/open/652803849) ^rw652803849
