# Delay accounting: an underrated feature of the Linux kernel

![rw-book-cover](https://coroot.com/static/img/blog/delay_accounting.png)
<br>
>[!note]- Readwise Information
>Title:: Delay accounting: an underrated feature of the Linux kernel
>Author:: [[coroot.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2022-03-09]]
>Last-Highlighted-Date:: [[2023-08-07]]
>Readwise-Link:: https://readwise.io/bookreview/22522784
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://coroot.com/blog/linux-delay-accounting
--- 

## Linked Notes
```dataview
LIST
FROM [[Delay accounting: an underrated feature of the Linux kernel by coroot.com Highlights]]
```

---

## Highlights
- Nowadays, in the era of microservices, infrastructures have become super-complex: dynamic nodes provisioning, autoscaling, dozens or even hundreds of containers working side by side. In order to maintain control over such infrastructure, we need to be able to know what has happened to each application at any given time. [View Highlight](https://readwise.io/open/576239506) ^rw576239506
- First, let's look at computing resources. Usually, when engineers talk about resources, they are actually referring to utilization which is not always correct. For example, the high utilization of a CPU by a container is not an issue in general. The real problem here is that this can cause another container on the same machine to perform slower due to a lack of CPU time. [View Highlight](https://readwise.io/open/576239507) ^rw576239507
