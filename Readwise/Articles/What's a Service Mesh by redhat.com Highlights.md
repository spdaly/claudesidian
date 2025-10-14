# What's a Service Mesh?

![rw-book-cover](https://www.redhat.com/profiles/rh/themes/redhatdotcom/img/red-hat-social-share.jpg)
<br>
>[!note]- Readwise Information
>Title:: What's a Service Mesh?
>Author:: [[redhat.com]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2018-06-29]]
>Last-Highlighted-Date:: [[2023-03-07]]
>Readwise-Link:: https://readwise.io/bookreview/25091453
>Readwise-Source:: #Readwise/source/reader
>Document-Tags:: [[software-architecture]] 
>Source URL:: https://www.redhat.com/en/topics/microservices/what-is-a-service-mesh
--- 

## Linked Notes
```dataview
LIST
FROM [[What's a Service Mesh? by redhat.com Highlights]]
```

---

## Highlights
- A service mesh, like the open source project [Istio,](https://www.redhat.com/en/topics/microservices/what-is-istio) is a way to control how different parts of an application share data with one another. [View Highlight](https://readwise.io/open/488013965) ^rw488013965
- a service mesh is a dedicated infrastructure layer built right into an app. [View Highlight](https://readwise.io/open/488014198) ^rw488014198
- Modern applications are often broken down in this way, as a network of services each performing a specific business function. [View Highlight](https://readwise.io/open/488014311) ^rw488014311
- A [microservices](https://www.redhat.com/en/topics/microservices/what-are-microservices) architecture lets developers make changes to an app’s services without the need for a full redeploy. [View Highlight](https://readwise.io/open/488014399) ^rw488014399
- microservices are built independently, communicate with each other, and can individually fail without escalating into an application-wide outage. [View Highlight](https://readwise.io/open/488014404) ^rw488014404
- Service-to-service communication is what makes microservices possible. The logic governing communication *can* be coded into each service without a service mesh layer—but as communication gets more complex, a service mesh becomes more valuable. [View Highlight](https://readwise.io/open/488014413) ^rw488014413
- a service mesh is that it takes the logic governing service-to-service communication out of individual services and abstracts it to a layer of infrastructure [View Highlight](https://readwise.io/open/488014522) ^rw488014522
- ndividual proxies that make up a service mesh are sometimes called "sidecars," since they run *alongside* each service, rather than *within* them [View Highlight](https://readwise.io/open/488014557) ^rw488014557
- Note: How is a service mesh implemented?
- Without a service mesh, each microservice needs to be coded with logic to govern service-to-service communication, which means developers are less focused on business goals. It also means communication failures are harder to diagnose because the logic that governs interservice communication is hidden within each service [View Highlight](https://readwise.io/open/488014586) ^rw488014586
- Note: Why do I need a service mesh?
- a service mesh also captures every aspect of service-to-service communication as performance metrics. Over time, data made visible by the service mesh can be applied to the rules for interservice communication, resulting in more efficient and reliable service requests. [View Highlight](https://readwise.io/open/488014648) ^rw488014648
