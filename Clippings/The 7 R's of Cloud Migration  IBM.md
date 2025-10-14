---
title: "The 7 R's of Cloud Migration | IBM"
source: "https://www.ibm.com/think/insights/7-rs-cloud-migration"
author:
  - "[[Stephanie Susnjara]]"
  - "[[Ian Smalley]]"
published:
created: 2025-10-14
description: "The 7 R’s of cloud migration (Rehost, Relocate, Replatform, Refactor, Repurchase, Retire and Retain) represent seven strategic approaches for moving applications and workloads to the cloud."
tags:
  - "clippings"
---
My IBM Subscribe

## Authors

Staff Writer

IBM Think

Staff Editor

IBM Think

Each application has its own architecture, dependencies and business needs. The 7 R’s framework helps organizations evaluate each situation individually and select the migration path that best balances speed, cost-efficiency and long-term value.

forms the foundation for how most modern businesses operate. Financial institutions process millions of transactions daily through cloud infrastructures, while retailers manage inventory and customer data across global operations. In healthcare, providers store and analyze patient records on cloud platforms that maintain strict privacy and security standards. Manufacturing companies rely on these same systems to monitor production lines and supply chains in real time, enabling them to respond swiftly to disruptions.

As cloud adoption accelerates across industries, organizations need strategic approaches to manage their migration journeys.

This environment is where frameworks like the 7 R’s become essential. The widespread reliance on cloud across industries underscores the growing demand for scalable and flexible cloud environments.

Cloud applications run on infrastructure, offering on-demand access to scalable computing resources like servers, , , development tools and , all delivered over the internet with flexible, pay-as-you-go pricing.

The global cloud market reflects this shift, valued at USD 752.44 million in 2024 and projected to grow to USD 2,390.19 billion by 2030.<sup>1</sup> The rising adoption of and is driving this growth, as both technologies require robust .

Industry newsletter

### The latest tech news, backed by expert insights

Stay up to date on the most important—and intriguing—industry trends on AI, automation, data and beyond with the Think newsletter. See the [IBM Privacy Statement](https://www.ibm.com/us-en/privacy).

Your subscription will be delivered in English. You will find an unsubscribe link in every newsletter. You can manage your subscriptions or unsubscribe [here](https://www.ibm.com/account/reg/signup?formid=news-urx-51525). Refer to our [IBM Privacy Statement](https://www.ibm.com/us-en/privacy) for more information.  

## Origin of the 7 R's

The 7 R’s evolved from the initial 5 R’s framework (rehost, refactor, revise, rebuild and replace) introduced in 2010 by Gartner, Inc. These strategies were launched at a time when organizations were just beginning to realize the potential of cloud computing, but faced the challenge of moving on-premises legacy applications to this new environment. The 5 R’s served as a roadmap to help companies classify their applications for migration.

As cloud adoption matured, Amazon Web Services (AWS) expanded the framework in 2016 by adding a sixth R: Retire. This addition recognized that migration projects often reveal applications that are no longer needed, presenting an opportunity to eliminate unnecessary costs rather than migrating everything.

In 2017, the framework evolved further with AWS’s addition of the seventh R: Retain. Today, most enterprise businesses use and strategies, where some applications remain on-premises while others move to the cloud.

The complete 7 R’s framework now provides comprehensive guidance for a full range of migration approach decisions.

### Achieving AI-readiness with hybrid cloud

## What is cloud migration?

Cloud migration is the process of migrating applications, data, workloads and from on-premises to cloud-based infrastructure.

Organizations migrate to the cloud to take advantage of benefits like cost optimization, improved scalability, ), improved and access to advanced technologies like AI and ML.

The decision to migrate often comes when organizations face aging infrastructure, rising data center costs or the need to support remote workforces. Some move to the cloud to enable faster innovation and deployment cycles. Others migrate to meet growing data storage demands or to leverage features that aren’t feasible on-premises.  
  

## Types of cloud migration

Cloud migration types come in different forms depending on where applications are moving and why. They include the following categories:

- Data center migration
- Hybrid cloud migration
- Cloud-to-cloud migration
- Multicloud migration
- Workload-specific migration

### Data center migration

In a data center migration, organizations move their entire infrastructure to the cloud, consolidating physical servers and storage into cloud resources. This shift often occurs when companies want to end expensive data center leases or eliminate the burden of maintaining on-premises hardware.

### Hybrid cloud migration

Hybrid cloud migration keeps some workloads on-premises while moving others to the cloud. This approach works well when regulatory requirements dictate that certain applications stay on-premises while others benefit from cloud capabilities.

According to an IBM Institute for Business Value (IBV) report titled [Mastering Hybrid Cloud](https://www.ibm.com/downloads/cas/DAEL0EQY), organizations that adopt a hybrid cloud approach can achieve notably greater value. In fact, they can realize 2.5 times more value compared to relying solely on a single public cloud platform.

### Cloud-to-cloud migration

In this scenario, apps and data move from one cloud provider (for example, AWS, IBM Cloud®, Microsoft Azure, Google Cloud Platform) to another or between different cloud services within the same provider.

Organizations choose this path to avoid vendor lock-in, take advantage of better pricing or access-specific platform features that better suit their needs.

### Multicloud migration

With a multicloud strategy, organizations distribute workloads across multiple providers tap into each platform’s strengths and optimize costs. This approach provides flexibility and reduces dependency on any single vendor.

### Workload-specific migration

This approach focuses on moving particular workloads, or to take advantage of cloud benefits. Organizations often start here when they want to modernize specific systems without committing to a full migration process right away.

## Challenges of cloud migration

Moving to the cloud introduces several challenges that make a structured strategy essential. Legacy systems often have complex, undocumented dependencies that make it difficult to understand the full impact of migrating them. Performance issues can emerge when applications designed for on-premises infrastructure don’t work optimally in cloud environments. Moreover, network can impact applications that require real-time data processing or frequent communication between components.

Security and compliance concerns require careful planning to ensure that and regulatory requirements are met in the cloud. According to an [IBM IBV 2023 report](https://www.ibm.com/thought-leadership/institute-business-value/report/data-story-hybrid-cloud-ai), skills gaps present a significant hurdle, with approximately 58% of global decision-makers reporting that cloud skills remain a considerable challenge. Without proper governance, cloud costs can spiral as teams spin up resources without understanding the pricing implications.

## Understanding the 7 R's of cloud migration

Each of the 7 R’s represents a distinct migration strategy with specific use cases and tradeoffs.

1. Rehost (lift-and-shift)
2. Relocate
3. Replatform
4. Refactor (rearchitect)
5. Repurchase (drop-and-shop)
6. Retire
7. Retain (revisit)

### 1\. Rehost (Lift-and-shift)

Rehosting moves applications to the cloud without changing the application code or architecture (this approach is also known as ). Applications transfer as-is from on-premises infrastructure to cloud infrastructure, typically through .

This strategy works best when organizations need to migrate quickly, lack resources to rearchitect applications or want to realize immediate cloud benefits like reduced data center costs.

### 2\. Relocate

Relocating transfers workloads by moving virtual machines directly between environments without modifying applications. This approach typically involves moving -based workloads to cloud environments.

Organizations with significant investments in VMware infrastructure can use this strategy to quickly migrate virtual machines with their existing layer intact, while maintaining operational consistency.

### 3\. Replatform

Replatforming makes targeted optimizations to applications during migration to take advantage of cloud capabilities without changing the core architecture.

Common examples include migrating databases to managed services like Amazon RDS or apps.

### 4\. Refactor (Rearchitect)

Refactoring reimagines how developers build applications by completely rearchitecting them into cloud-native solutions. This process typically involves breaking monolithic applications into or adopting . These architectures work well with practices, enabling and deployment.

Organizations choose this strategy when they need to add features that are difficult with the current architecture, when applications need significant scalability improvements or when long-term operational efficiency justifies the upfront investment.

### 5\. Repurchase (Drop-and-shop)

Repurchasing replaces existing applications with cloud-based alternatives. Instead of migrating existing software, organizations adopt a new solution that’s already cloud-native.

This strategy makes sense for applications where commercial SaaS offerings provide equivalent or better features. It’s also a logical approach when legacy applications would cost more to migrate than adopting a SaaS alternative.

### 6\. Retire

Retiring involves identifying and decommissioning applications that are no longer needed. Cloud migration projects often reveal that certain applications have minimal business value relative to their cost.

Organizations retire applications when usage data reveals minimal adoption, other systems replace their capabilities or migration costs outweigh their business value.

### 7\. Retain (Revisit)

Retaining means keeping applications in their current environment, at least for now. These applications stay on-premises with plans to revisit the migration decision later. This strategy applies to applications that are recently upgraded and stable, applications with compliance requirements that need resolution before migration, or applications with complex dependencies requiring more planning time.

## Creating a cloud migration strategy

Developing an effective [cloud migration strategy](https://www.ibm.com/think/insights/cloud-migration-strategy) starts with comprehensive discovery and assessment. Organizations need to inventory all applications, understand their dependencies and evaluate business criticality. This assessment determines which of the 7 R’s makes sense for each application.

Organizations typically begin with applications that offer quick positive results, such as systems that are straightforward to migrate and deliver immediate value. This builds momentum, develops team capabilities and demonstrates cloud benefits. High-risk or complex applications usually migrate later after teams have accumulated cloud expertise.

Migration plans for each application should include success criteria, rollback procedures, data migration planning and coordination with business stakeholders on timing.

Testing strategies need special attention. Applications require thorough testing in cloud environments to ensure compatibility before going live, and many organizations run parallel environments during transition periods to reduce risk.

Governance and cost management frameworks should be established before migration begins. Cloud spending can grow rapidly without proper controls. Resource tagging, budget alerts and regular cost reviews help organizations optimize cloud spending and avoid surprises.

## Cloud migration tools and partners

Cloud providers offer various tools to support migration. AWS cloud migration tools, such as AWS Application Migration Service, simplify lift-and-shift migrations by automatically converting source servers, while IBM Cloud provides migration services and tools for assessing and moving workloads. Azure Migrate and similar services help move databases with minimal downtime, and tracking tools provide centralized visibility into migration progress across multiple workloads.

Beyond providing tools, ecosystem partners extend cloud capabilities with specialized expertise and services. Major technology companies like IBM and Microsoft offer consulting services and migration tools that help organizations assess their portfolios, plan migrations and optimize cloud deployments.

Analytics platforms provide planning tools for estimating operational costs, managed service providers offer hands-on migration assistance and system integrators bring deep expertise in specific industries or application types.

Choosing the right combination of services, tools and partners depends on factors like migration size and complexity, internal team capabilities, budget constraints and timeline requirements.

## Conclusion

A successful cloud migration isn’t just about moving infrastructure—it’s about transforming how an organization operates. The 7 R’s framework, when paired with the right cloud services, empowers organizations to align each workload with the most effective migration path. This approach ensures that every application contributes to business agility, operational efficiency and long-term innovation.

[Rethink application modernization with generative AI](https://www.ibm.com/account/reg/signup?formid=urx-52503)

[Discover how IBM and AWS can help CIOs unlock innovation and value in application modernization with AI.](https://www.ibm.com/account/reg/signup?formid=urx-52503)

[Kickstart your cloud migration journey](https://www.ibm.com/downloads/documents/us-en/10c31775a05401cb)

[Access essential insights on cloud migration with IBM’s latest report. Discover the top 10 facts every tech leader needs to know.](https://www.ibm.com/downloads/documents/us-en/10c31775a05401cb)

Related solutions

## Related solutions

Cloud Migration - IBM Instana Observability

Instana simplifies your cloud migration journey by offering comprehensive monitoring and actionable insights.

[Explore Instana](https://www.ibm.com/products/instana/cloud-migration) Migrate to IBM Cloud

Migrate to the IBM Cloud with customizable solutions and tools to accelerate your journey.

[Explore cloud migration](https://www.ibm.com/cloud/migrate) Cloud Migration Consulting

IBM Cloud Migration Services helps manage cloud migration for your business, enabling digital transformation.

[Cloud migration services](https://www.ibm.com/consulting/cloud-migration)

Take the next step

Accelerate your cloud migration journey with expert consulting services from IBM. Discover how our solutions can help you transition to the cloud efficiently, or book a live demo to see the benefits of IBM Turbonomic in action.

[Explore IBM Cloud Migration Services](https://www.ibm.com/consulting/cloud-migration) [Book a live demo](https://www.ibm.com/account/reg/signup?formid=DEMO-automateturbonomic)

##### Footnotes

1\. [Cloud Computing Market (2025–2030)](https://www.grandviewresearch.com/horizon/outlook/cloud-computing-market-size/global), Grand view research, 2024

The chat window has been closed