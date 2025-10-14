# CTOs’ Guide to Containers and Kubernetes — Answering the Top 10 FAQs

![rw-book-cover](https://emtemp.gcom.cloud/ngw/globalassets/gartner-tile.jpg)
<br>
>[!note]- Readwise Information
>Title:: CTOs’ Guide to Containers and Kubernetes — Answering the Top 10 FAQs
>Author:: [[Gartner]]
>Type:: #Readwise/category/articles
>Published-Date:: [[2022-05-31]]
>Last-Highlighted-Date:: [[2023-02-20]]
>Readwise-Link:: https://readwise.io/bookreview/24589179
>Readwise-Source:: #Readwise/source/reader
>Source URL:: https://www.gartner.com/document/4015168?ref=solrAll&refval=356191823
--- 

## Linked Notes
```dataview
LIST
FROM [[CTOs’ Guide to Containers and Kubernetes — Answering the Top 10 FAQs by Gartner Highlights]]
```

---

## Highlights
- By 2027, more than 90% of global organizations will be running containerized applications in production, which is a significant increase from fewer than 40% in 2021.
  By 2027, 25% of all enterprise applications will run in containers, an increase from fewer than 10% in 2021.
  By 2027, more than 65% of commercial-of-the-shelf (COTS) vendors will offer their software in container format, up from less than 20% in 2021. [View Highlight](https://readwise.io/open/479489529) ^rw479489529
- Containers and Kubernetes have significantly grown in popularity and adoption over the past five years. While container technology has been in existence for more than a decade, its recent meteoric rise can be attributed to changes in software architecture and development patterns, growing adoption of DevOps and the fact that both containers and Kubernetes are open-source projects supported by a wide ecosystem of participants. In this research, we answer the most common client questions about containers and Kubernetes that will help enterprise architecture and technology innovation leaders benefit from and operationalize these technologies. [View Highlight](https://readwise.io/open/479489541) ^rw479489541
- 1. What are some of the key benefits of containers and Kubernetes?
  Containers and Kubernetes can bring several benefits to an organization. Some of the key benefits are:
  • Agile application development and deployment: Containers help simplify application packaging and enable a rapid application deployment process with the ability to do frequent application builds, quick software release and granular rollbacks. The ability to develop and deploy software faster can have a significant impact on top-line growth and customer experience.
  • Environmental consistency: Through tight application component packaging, containers enable platform consistency across development, testing, staging and production clusters. This is an important driver of developer productivity and service resiliency.
  • Immutability: Containers should be deployed in an immutable way using declarative principles — which means that there won’t be any out of process changes or patches. This makes container deployments highly repeatable, automated and secure with lower operational overheads.
  • Flexibility and choice: Kubernetes is supported by a huge ecosystem of cloud providers, ISVs and IHVs. This API and cross-platform consistency, open-source innovation and industry support offers a great degree of flexibility for CTOs. [View Highlight](https://readwise.io/open/479489676) ^rw479489676
- • Platform complexity: While containers and Kubernetes can be used for many use cases today, they don’t need to be used in every case. Using Kubernetes to orchestrate static, COTS applications can be overkill due to the inherent complexity of Kubernetes that would overshadow any meaningful business benefits that may accrue. Similarly, deploying it for performance-sensitive and stateful applications requires significant know-how and operational maturity.
  • Security: While there is nothing inherent in the container technology that makes it unsecure, deploying it at scale requires a mature DevSecOps process and shared responsibility between developers, platform operations, SRE and security teams.
  • Automation and governance: Successful container deployments require extensive and continuous curation of technology components, consistent operations and upgrade of existing tools and processes to ensure automation and governance. This necessitates investments in new tooling and removing any constraints in enabling an agile environment — which can often lead to conflicting opinions across teams, as well as a laborious time-consuming selection and integration process.
  • Culture and skills: Organizations face steep challenges in building containerized apps and operationalizing them due to a dearth of skills across development, security and operations teams. Moreover, deploying a common platform like Kubernetes requires clearly defined shared responsibilities across teams and a growth mindset that can tolerate failures and iterate accordingly. [View Highlight](https://readwise.io/open/479492239) ^rw479492239
- • **Microservices**: Microservices application architecture is characterized by independent application components that are distributed and loosely coupled. Containers and Kubernetes enable a strong foundation architecture for microservices due to their ability to orchestrate these modular services, enable scaling and self-healing of the services, and create a layer of service isolation.
  • **DevOps enabler**: Containers enable a CI/CD process by isolating code into a discrete unit, which makes it easier for developers and DevOps teams to modify and update the code across the software development life cycle.
  • **Application portability (or lock-in risk reduction):** The runtime parity of containers, and the ubiquitous availability of Kubernetes, enable developers to build apps that can run in a consistent way across hybrid or multicloud environments. While complete application portability is usually not possible because most applications have dependencies outside containers and Kubernetes, organizations can reduce the vendor lock-in risk.
  • **Legacy app** **modernization:** You can take advantage of the more efficient deployment and service isolation of containers by modernizing and streamlining the life cycle management legacy applications. However, simple, lift-and-shift types of migrations are usually only feasible for lightweight workloads. [View Highlight](https://readwise.io/open/479492417) ^rw479492417
- • Low degree of external application dependencies
  • The infrastructure and platform technologies that the application runs on are already available as container images (i.e., Linux, Tomcat, NGINX, PostgreSQL, etc.)
  • Preferably stateless apps for initial deployments
  • Application has rapid elasticity needs and requires frequent code changes
  • If you deploy a COTS application, there is a vendor supported image for it [View Highlight](https://readwise.io/open/479493286) ^rw479493286
