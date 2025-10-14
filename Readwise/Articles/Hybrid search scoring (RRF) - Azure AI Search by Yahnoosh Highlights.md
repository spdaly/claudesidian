# Hybrid search scoring (RRF) - Azure AI Search

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_174804/open-graph-image_pJlTm1k.png)
<br>
>[!note]- Readwise Information
>Title:: Hybrid search scoring (RRF) - Azure AI Search
>Author:: [[Yahnoosh]]
>Type:: #Readwise/category/articles
>Published-Date:: [[]]
>Last-Highlighted-Date:: [[2024-06-04]]
>Readwise-Link:: https://readwise.io/bookreview/41187569
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
--- 

## Linked Notes
```dataview
LIST
FROM [[Hybrid search scoring (RRF) - Azure AI Search by Yahnoosh Highlights]]
```

---

## Highlights
- Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores from multiple, previously ranked results to produce a unified result set. [View Highlight](https://readwise.io/open/729113386) ^rw729113386
- RRF is used to merge and homogenize the rankings into a single result set, returned in the query response. [View Highlight](https://readwise.io/open/729113441) ^rw729113441
- RRF works by taking the search results from multiple methods, assigning a reciprocal rank score to each document in the results, and then combining the scores to create a new ranking. [View Highlight](https://readwise.io/open/729113498) ^rw729113498
- Only fields marked as `searchable` in the index, or `searchFields` in the query, are used for scoring. Only fields marked as `retrievable`, or fields specified in `select` in the query, are returned in search results, along with their search score. [View Highlight](https://readwise.io/open/729113544) ^rw729113544
