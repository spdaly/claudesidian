# Reference 2: Introducing the Command Query Responsibility Segregation Pattern

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)
<br>
>[!note]- Readwise Information
>Title:: Reference 2: Introducing the Command Query Responsibility Segregation Pattern
>Author:: [[Archiveddocs]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2014-05-08]]
>Last-Highlighted-Date:: [[2022-12-31]]
>Readwise-Link:: https://readwise.io/bookreview/22702110
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://learn.microsoft.com/en-us/previous-versions/msp-n-p/jj591573(v=pandp.10)
--- 

## Linked Notes
```dataview
LIST
FROM [[Reference 2: Introducing the Command Query Responsibility Segregation Pattern by Archiveddocs Highlights]]
```

---

## Highlights
- CQRS is simply the creation of two objects where there was previously only one. The separation occurs based upon whether the methods are a command or a query (the same definition that is used by Meyer in Command and Query Separation: a command is any method that mutates state and a query is any method that returns a value). [View Highlight](https://readwise.io/open/446418992) ^rw446418992
- "CQRS is a simple pattern that strictly segregates the responsibility of handling command input into an autonomous system from the responsibility of handling side-effect-free query/read access on the same system. Consequently, the decoupling allows for any number of homogeneous or heterogeneous query/read modules to be paired with a command processor. This principle presents a very suitable foundation for event sourcing, eventual-consistency state replication/fan-out and, thus, high-scale read access. In simple terms, you don't service queries via the same module of a service that you process commands through. In REST terminology, GET requests wire up to a different thing from what PUT, POST, and DELETE requests wire up to." [View Highlight](https://readwise.io/open/446419020) ^rw446419020
- CQRS is an architectural style that is often enabling of DDD [View Highlight](https://readwise.io/open/446419359) ^rw446419359
- • Models should be bound to the implementation.
  • You should cultivate a language based on the model.
  • Models should be knowledge rich.
  • You should brainstorm and experiment to develop the model. [View Highlight](https://readwise.io/open/446419798) ^rw446419798
- DDD is an analysis and design approach that encourages you to use models and a ubiquitous language to bridge the gap between the business and the development team by fostering a common understanding of the domain. [View Highlight](https://readwise.io/open/446420383) ^rw446420383
- DDD approach is oriented towards analyzing behavior rather than just data in the business domain, and this leads to a focus on modeling and implementing behavior in the software. A natural way to implement the domain model in code is to use commands and events. This is particularly true of applications that use a task-oriented UI. [View Highlight](https://readwise.io/open/446420522) ^rw446420522
- In many enterprise systems, the number of reads vastly exceeds the number of writes, so your scalability requirements will be different for each side. By separating the read side and the write side into separate models within the bounded context, you now have the ability to scale each one of them independently. [View Highlight](https://readwise.io/open/446423072) ^rw446423072
- Adopting the CQRS pattern helps you to focus on the business and build task-oriented UIs. A consequence of separating the different concerns into the read side and the write side is a solution that is more adaptable in the face of changing business requirements. This results in lower development and maintenance costs in the longer term. [View Highlight](https://readwise.io/open/446423123) ^rw446423123
- Facilitates building task-based UIs [View Highlight](https://readwise.io/open/446423132) ^rw446423132
