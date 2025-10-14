# Better RAG Results With Reciprocal Rank Fusion and Hybrid Search

![rw-book-cover](https://cdn.prod.website-files.com/610225ff318d106f5343df0c/66561437c63a3e0fd533932a_Blog_Better%20RAG%20results%20with%20Reciprocal%20Rank%20Fusion%20and%20Hybrid%20Search_tb.png)
<br>
>[!note]- Readwise Information
>Title:: Better RAG Results With Reciprocal Rank Fusion and Hybrid Search
>Author:: [[John Wang]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2024-05-28]]
>Last-Highlighted-Date:: [[2024-06-04]]
>Readwise-Link:: https://readwise.io/bookreview/41187555
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[retrieval augmented generation]] [[search]] [[technology]] 
>Source URL:: https://www.assembled.com/blog/better-rag-results-with-reciprocal-rank-fusion-and-hybrid-search
--- 

## Linked Notes
```dataview
LIST
FROM [[Better RAG Results With Reciprocal Rank Fusion and Hybrid Search by John Wang Highlights]]
```

---

## Highlights
- To enable a hybrid store solution, we developed a document store abstraction in our code, allowing us to integrate multiple search algorithms. The abstraction is simple but captures all the essential functionalities of a document store and search system. It handles document management and querying and is agnostic to the actual implementation (vector search, keyword search, etc.). Here’s what it looks like: [View Highlight](https://readwise.io/open/729113257) ^rw729113257 
- See also: [[👻 ai highlighted]] 
- The interesting part is that our hybrid search store itself implements the **`DocumentStore`** interface. This means that, from the perspective of the caller, it doesn't matter whether they are interacting with a single store or our complex hybrid store — they use the same interface and methods. This design ensures that all of the logic for determining which documents are retrieved is hidden from the caller and can be tested separately. To implement the hybrid store, we passed in multiple child document stores and parallelized the search across all of the child stores. [View Highlight](https://readwise.io/open/729113258) ^rw729113258 
- See also: [[👻 ai highlighted]] 
- Reciprocal Rank Fusion [View Highlight](https://readwise.io/open/729113303) ^rw729113303
