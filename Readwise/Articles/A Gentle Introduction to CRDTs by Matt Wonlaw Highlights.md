# A Gentle Introduction to CRDTs

![rw-book-cover](https://vlcn.io/assets/hero.png)
<br>
>[!note]- Readwise Information
>Title:: A Gentle Introduction to CRDTs
>Author:: [[Matt Wonlaw]]
>Type:: #Readwise/category/articles
>Published-Date:: [[]]
>Last-Highlighted-Date:: [[2023-02-13]]
>Readwise-Link:: https://readwise.io/bookreview/24344187
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://vlcn.io/blog/gentle-intro-to-crdts.html
--- 

## Linked Notes
```dataview
LIST
FROM [[A Gentle Introduction to CRDTs by Matt Wonlaw Highlights]]
```

---

## Highlights
- A CRDT is a data structure that is replicated across multiple computers in a network, with the following features:
  1. The application can update any replica independently, concurrently and without coordinating with other replicas.
  2. An algorithm (itself part of the data type) automatically resolves any inconsistencies that might occur.
  3. Although replicas may have different state at any particular point in time, they are guaranteed to eventually converge. [View Highlight](https://readwise.io/open/475436728) ^rw475436728
- CRDTs are needed in situations where you want multiple processes to modify the same state without coordinating their writes to that state. [View Highlight](https://readwise.io/open/475436820) ^rw475436820
- Even in situations where you do have excellent connectivity, CRDTs are useful to present a realtime experience to users. CRDTs allow all writes to be processed locally and merged with remote nodes later rather than requiring round-trips to a server for every write. [View Highlight](https://readwise.io/open/475436846) ^rw475436846
