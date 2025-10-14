# Rationale for Mats

![rw-book-cover](https://mats3.io/assets/images/Mats3Logo-640x640.png)
<br>
>[!note]- Readwise Information
>Title:: Rationale for Mats
>Author:: [[Endre Stølsvik]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2023-02-12]]
>Last-Highlighted-Date:: [[2023-02-12]]
>Readwise-Link:: https://readwise.io/bookreview/24311122
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[software-architecture]] 
>Source URL:: https://mats3.io/background/rationale-for-mats/
--- 

## Linked Notes
```dataview
LIST
FROM [[Rationale for Mats by Endre Stølsvik Highlights]]
```

---

## Highlights
- Messaging naturally provides high availability, scalability, location transparency, prioritization, stage transactionality, fault tolerance, great monitoring, simple error handling, and efficient and flexible resource management. However, messaging can be much harder to employ in practice due to a fundamentally different programming model. [View Highlight](https://readwise.io/open/474940030) ^rw474940030
- In a microservice architecture one needs to communicate between the different services. [View Highlight](https://readwise.io/open/474940065) ^rw474940065
- *Asynchronous Message Oriented architectures* are superior to synchronous REST-based systems in a number of ways, for example: [View Highlight](https://readwise.io/open/474940090) ^rw474940090
- However, the big pain point with message-based communications is that to reap all these benefits, one need to fully embrace asynchronous, multi-staged distributed processing, where each stage is totally stateless, but where one still needs to maintain a state throughout the flow. [View Highlight](https://readwise.io/open/474940441) ^rw474940441
- ou gain much: Each of these stages are independent processes. There is no longer a distributed blocking state residing through multiple services, as the queues acts as intermediaries, each stage processor having fully performed its part of the total process before posting the (intermediate) result on a queue (and then goes back fetching a new message to process from its incoming queue) [View Highlight](https://readwise.io/open/474943524) ^rw474943524
- With a Messaging-Oriented Architecture, each part of the total process would actually be a separate subprocess [View Highlight](https://readwise.io/open/474940644) ^rw474940644
- However, you also loose much: The simple service method where you could reason locally and code in a straight down manner, with state implicitly being handled by the ordinary machinery of the thread stack and local variables, now becomes a distributed process spread over several code bases, and any state needed between the process stages must be handled explicitly. [View Highlight](https://readwise.io/open/474944852) ^rw474944852
