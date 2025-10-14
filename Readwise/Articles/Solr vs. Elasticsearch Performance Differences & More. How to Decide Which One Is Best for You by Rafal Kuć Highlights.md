# Solr vs. Elasticsearch: Performance Differences & More. How to Decide Which One Is Best for You

![rw-book-cover](https://sematext.com/wp-content/uploads/2022/01/Solr-vs.-Elasticsearch_-Performance-Differences-More.png)
<br>
>[!note]- Readwise Information
>Title:: Solr vs. Elasticsearch: Performance Differences & More. How to Decide Which One Is Best for You
>Author:: [[Rafal Kuć]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2022-01-07]]
>Last-Highlighted-Date:: [[2023-02-28]]
>Readwise-Link:: https://readwise.io/bookreview/24857820
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://sematext.com/blog/solr-vs-elasticsearch-differences/
--- 

## Linked Notes
```dataview
LIST
FROM [[Solr vs. Elasticsearch: Performance Differences & More. How to Decide Which One Is Best for You by Rafal Kuć Highlights]]
```

---

## Highlights
- Elasticsearch and Solr are two of the leading, competing open source search engines known to anyone who has ever looked into (open source) search. They are both built around the core underlying search library – [Lucene](https://lucene.apache.org/) – but they are different in terms of functionalities such as scalability, ease of deployment, as well as community presence and many more. Solr has more advantages when it comes to the static data, because of its caches and the ability to use an uninverted reader for faceting and sorting – for example, e-commerce. On the other hand, Elasticsearch is better suited – and much more frequently used – for timeseries data use cases, like [log analysis](https://sematext.com/logsene) use cases. [View Highlight](https://readwise.io/open/484027604) ^rw484027604
- For 95% of use cases either choice will be just fine in terms of performance, and the remaining 5% need to test both solutions with their particular data and their particular access patterns. [View Highlight](https://readwise.io/open/484027623) ^rw484027623
- In Solr, you need the *managed-schema* file (former *schema.xml*) in order to define how your index structure, to define fields and their types. [View Highlight](https://readwise.io/open/484028113) ^rw484028113
- Elasticsearch is a bit different – it can be called schemaless. [View Highlight](https://readwise.io/open/484028126) ^rw484028126
- [Elasticsearch](https://sematext.com/guides/elasticsearch/) is very dynamic as far as placement of indices and shards they are built of is concerned. [View Highlight](https://readwise.io/open/484028411) ^rw484028411
- Another major difference between Elasticsearch and Solr is the node discovery and cluster management in general. The main purpose of discovery is to monitor nodes’ states, choose master nodes, and in some cases also store shared configuration files. [View Highlight](https://readwise.io/open/484028093) ^rw484028093
- Solr tends to be more static out of the box. [View Highlight](https://readwise.io/open/484028477) ^rw484028477
