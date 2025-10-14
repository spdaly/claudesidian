# Using eBPF and Predefined Inspections to Minimize "Observability Tax"

![rw-book-cover](https://coroot.com/static/img/blog/observability-tax/teaser.png)
<br>
>[!note]- Readwise Information
>Title:: Using eBPF and Predefined Inspections to Minimize "Observability Tax"
>Author:: [[Nikolay Sivko]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2022-12-23]]
>Last-Highlighted-Date:: [[2022-12-27]]
>Readwise-Link:: https://readwise.io/bookreview/22522740
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://coroot.com/blog/minimizing-observability-tax
--- 

## Linked Notes
```dataview
LIST
FROM [[Using eBPF and Predefined Inspections to Minimize "Observability Tax" by Nikolay Sivko Highlights]]
```

---

## Highlights
- Observability is a critical aspect of any infrastructure, as it allows teams to identify and troubleshoot issues quickly. However, making a system observable is not without its costs. It's quite a time- and resource-consuming process since it requires adding instrumentation into every application. [View Highlight](https://readwise.io/open/443032949) ^rw443032949
- My optimistic estimate is that it can take over 40 hours for an *experienced* engineer to instrument a system of 10 services. Keep in mind, however, that you will have to repeat most of these steps every time you run a new service. I think the term *"observability tax"* is particularly well-suited to describe the costs that companies have to incur in terms of time, resources, and effort if they want to maintain a high level of visibility into their infrastructures. [View Highlight](https://readwise.io/open/443032979) ^rw443032979
- [eBPF](https://ebpf.io) (extended Berkeley Packet Filter) is a game-changing technology that can eliminate the need to manually instrument application code. It allows users to attach custom programs to various parts of the Linux kernel, such as system calls, network functions, and tracepoints. Such eBPF programs can be used for a wide range of purposes, including networking, security, and observability. [View Highlight](https://readwise.io/open/443033015) ^rw443033015
- While it is important to collect the right metrics, it is equally important to have a way to analyze and interpret the data in order to gain insights. [View Highlight](https://readwise.io/open/443033025) ^rw443033025
- To effectively troubleshoot an issue with a particular service, it is essential to have all relevant information about it in one place. [View Highlight](https://readwise.io/open/443033339) ^rw443033339
