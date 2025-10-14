---
title: "How to Choose the Right Approach for Application Modernization and Cloud Migration"
source: "https://www.gartner.com/document-reader/document/code/772600?ref=ddisp&refval=772600"
author:
published:
created: 2025-10-14
description: "Each of the application modernization and cloud migration approaches varies substantially in terms of scope and effect. Enterprise application leaders should use Gartner’s evaluation framework to select an approach that will produce the desired results, with acceptable cost, risk and impact."
tags:
  - "clippings"
---
## Overview

---

### Key Findings

- Enterprise application leaders often pursue modernization or cloud migration efforts without determining why and how an application poses an obstacle to digital business — leading them to select an approach that does not resolve the underlying problem.
- Without a clear understanding of the root cause of the problem and the effect of different modernization approaches, enterprise application leaders may select an ineffective approach that wastes time and effort, and will negatively impact business outcomes.

## Introduction

---

The 2023 Gartner CIO and Technology Executive Survey results show that 46% of the organizations will increase their spend on application modernization (the top four technology area in spending) and 50% will increase their spend on cloud platforms in 2023 (the top three technology area in spending). Also, 47% will decrease investments in legacy infrastructure and data center technologies, illustrating the transition to modern technology platforms.

Application portfolios deteriorate over time and gradually lose business fitness, innovation support and agility while becoming increasingly expensive, complex and risky. Enterprise application leaders can use various approaches to continuously improve the fitness and value of their applications so that they can better support changing business demands.

Which application modernization or cloud migration approach should you use? Enterprise application leaders should evaluate all five modernization and migration approaches, and use Gartner’s evaluation framework to choose the approach that solves that application’s problem and meets the organization’s acceptable level of risk, cost and impact.

## Analysis

---

### Establish a Clear Understanding of Application Modernization and Cloud Migration Approaches

### Table 1: Main Application Modernization and Cloud Migration Approaches

<table><tbody><tr><td colspan="1"><p><span><strong>Name</strong></span></p></td><td colspan="1"><p><span><strong>Alternative Names</strong></span></p></td><td colspan="1"><p><span><strong>Description</strong></span></p></td></tr><tr><td colspan="1"><p><span><strong>Rehost</strong></span></p></td><td colspan="1"><p><span><span>“Lift and shift,” redeploy</span></span></p></td><td colspan="1"><p><span><span>Redeploy </span><span>the application to other infrastructure (physical, virtual or cloud) without recompiling, modifying the application code, or modifying its features and functions.</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Replatform</strong></span></p></td><td colspan="1"><p><span><span>“Lift and reshape,” revise</span></span></p></td><td colspan="1"><p><span><span>Migrate the application to a new runtime platform. May include minimal changes to code for compatibility with the new platform (e.g., to use cloud services or another database platform), but no changes to the code structure or the features and functions it provides.</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Rearchitect</strong></span></p></td><td colspan="1"><p><span><span>Re-engineer, refactor</span></span></p></td><td colspan="1"><p><span><span>Restructure and optimize existing code without changing its external behavior to remove technical debt and improve nonfunctional attributes and structure. Can include a shift to a new application architecture or platform to exploit new and better capabilities. Can include code </span><span>transformation</span> <span>or </span><span>refactoring</span><span>.</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Rebuild</strong></span></p></td><td colspan="1"><p><span><span>Rewrite, redesign</span></span></p></td><td colspan="1"><p><span><span>Rebuild or rewrite the application. This includes the possibility to create a like-for-like replacement of the application and </span><span>preserve its scope and specifications</span><span>.</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Replace</strong></span></p></td><td colspan="1"><p><span><span>Repurchasing, “drop and shop”</span></span></p></td><td colspan="1"><p><span><span>Eliminate the former application and replace it with a </span><span>COTS or SaaS solution</span><span>, taking new requirements and needs into account.</span></span></p></td></tr></tbody><tbody><tr><td colspan="3"></td></tr></tbody></table>

Source: Gartner (January 2023)

Modernization approaches differ in their ability to change the technological, architectural or functionality aspects of the application:

- **Rehost and replatform** allow changes to the technology platform on which the application is running. These approaches can solve problems caused by the **technology****.**
- **Rearchitect** allows changes to both the technology platform and the code structure of the application. These approaches can solve problems in the **technology and architecture** domains.
- **Rebuild and replace** allow functions and features to be changed or added. These approaches can solve problems in the **functional** domain and provide the opportunity to change **technology and architecture**.

Figure 1 illustrates which layers and aspects can be changed by each modernization approach.

![The graphic mentions a matrix of modernization and cloud migration approaches against the three main application layers: functionality, architecture and technology. ](https://www.gartner.com/resources/772600/772600/Figure_1_Modernization_Approaches_Differ_in_Their_Ability_to_Change_Aspects_of_the_Application.png)

Figure 1: Modernization Approaches Differ in Their Ability to Change Aspects of the Application

#### Other Approaches for Legacy Applications

Apart from the five main application modernization and cloud migration approaches, enterprise application leaders may evaluate alternative options when modernization or migration is not worthwhile. The choice to modernize/migrate or not is often made in a preceding application rationalization or application portfolio assessment initiative. These alternate options include:

- **R** **etain:** Leave the application as is (for now). Modernization or migration is not worthwhile because it would involve too much effort and ris k or the application is nearing retirement and should be tolerated for now.
- **Encapsulate****:** Capture the application’s data and functions and make them accessible as services via an API. This approach leverages and extends the application features and value, while implementation specifics are hidden behind the interface.
- **Retire:** Decommission the application, often as part of a replace scenario.

### Determine What Functional, Architectural and Technological Issues Need to Be Resolved

Before deciding which modernization or cloud migration approach works best, enterprise application leaders need to answer two questions:

- What are the main issues with the current application?
- What are the causes of those issues?

#### Identify the Issues Using the Six Drivers for Modernization

First, define the issues you are trying to solve. Gartner has identified six common drivers for application modernization: three business drivers and three IT drivers (see Figure 2). You can use these drivers to evaluate the application and define the issues.

![The graphic mentions six main drivers for application modernization: to increase business fit, innovation and agility, and to reduce cost, complexity and risk.
](https://www.gartner.com/resources/772600/772600/Figure_2_Six_Drivers_of_Application_Modernization.png)

Figure 2: Six Drivers of Application Modernization

From a business perspective, the three main drivers for application modernization are:

- **Business fit:** The application no longer meets current business requirements.
- **Innovation:** The application constrains the business from leveraging new business opportunities or addressing disruptions.
- **Agility:** The application and its supporting ecosystems are not able to keep up with the pace of change, or those changes may come with an unacceptable level of cost and risk.

From an IT perspective, the three main drivers for application modernization are:

- **Cost:** The total cost of operating, maintaining and changing the application is too high in relation to its business value.
- **Complexity:** The high complexity of the application creates various problems and is a major factor in maintainability as it impacts time, cost and risk of implementing changes.
- **Risk:** The application poses security, compliance, supportability and scalability risks. In older application platforms and languages, the risk of a skills shortage is often a major concern.

#### Identify the Cause of the Issues

The six drivers can also help to locate the probable cause of the issues. The issues can originate from three main layers of an application: its technology, its architecture and its functionality.

In most cases, the main drivers for modernization point to the possible root cause (as shown in Figure 3):

- Cost, complexity and risk issues are most likely caused by the **technology** used to build and support the application.
- Business fit and innovation support issues are most likely caused by the **functionality**.
- Agility and complexity issues are most likely caused by the **architecture** and structure of the application.

![The graphic mentions the connection between the issues and causes (functionality, architecture and technology) and understands which modernization approach to take based on that.
](https://www.gartner.com/resources/772600/772600/Figure_3_Identify_Cause_of_the_Issue_as_Basis_for_Selecting_Best_Modernization_Approach.png)

Figure 3: Identify Cause of the Issue as Basis for Selecting Best Modernization Approach

### Use Gartner’s Evaluation Framework to Choose the Right Approach for Each Application

After identifying the likely cause of the application’s issues, enterprise application leaders can determine whether they need to fix the technology, architecture and/or functionality aspects of the application. This will be the basis for selecting the best modernization approach.

Gartner’s framework for selecting the right application modernization and cloud migration approach is outlined in Figure 4. It lists each modernization and migration approach, and identifies the extent to which it can contribute to solving problems in technology, architecture or functionality. For example, rearchitecting an application component can solve technology and architecture issues, but it has limited value in solving functional problems. Rebuilding an application gives you the greatest opportunity and flexibility to improve technology, architecture and functionality.

![The graphic mentions how modernization approach is able to support changes in technology, architecture of functionality of an application, based on 5 Rs (rehost, replatform, rearchitect, rebuild and replace). They are listed with circles as low and progressing to high.
](https://www.gartner.com/resources/772600/772600/Figure_4_Gartners_Framework_for_Selecting_the_Right_Application_Modernization_and_Cloud_Migration_Approach.png)

Figure 4: Gartner’s Framework for Selecting the Right Application Modernization and Cloud Migration Approach

- **Potential business value:** Stakeholders often overestimate the potential value of a modernization or migration approach (for example, they expect that a replatform will increase business fit or agility). It is important to be clear about the potential business value of each approach.
- **Time to value:** Implementation time, and therefore time to value, differs for each modernization and migration approach.
- **Business disruption:** What is the impact of the modernization approach on the business processes it supports? Is retraining required, or business process redesign? For example, a COTS or SaaS solution replacement will have a high impact on business processes and user experience.
- **Risk****:** This refers to the risk level of executing the modernization and migration.

Enterprise application leaders should use this framework to create a shortlist of suitable modernization approaches. Discuss the selected approach with all stakeholders. Set expectations by making everyone aware of the scope, effect, outcomes and consequences of the modernization. The considerations and consequences must be evaluated and weighed to decide if modernization or migration is worthwhile, and which of the candidate approaches provides the best balance between value and effect against cost, risk and impact.

**The b** **ottom line:** Choose the application modernization and cloud migration approach that delivers improvements to the relevant application layers — technology, architecture and functionality — and has an acceptable risk, cost and impact profile.

## Evidence

---

**2023 Gartner CIO and Technology Executive Survey:** This survey was conducted to help CIOs and technology executives overcome digital execution gaps by empowering and enabling an ecosystem of internal and external digital technology producers. It was conducted online from 2 May through 25 June 2022 among Gartner Executive Programs members and other CIOs. Qualified respondents were each the most senior IT leader (e.g., CIO) for their overall organization or some part of their organization (for example, a business unit or region). The total sample was 2,203 respondents, with representation from all geographies and industry sectors (public and private). **Disclaimer:** Results of this survey do not represent global findings or the market as a whole, but reflect the sentiments of the respondents and companies surveyed.

## Note 1: Application and Application Components

---

In this research, we talk about an application as the target of modernization and cloud migration. The target can also be a component or module of an application. Gartner recommends an incremental approach to application modernization and cloud migration by focusing on the components of an application instead of a big-bang modernization of the whole application. This implies that components of an application should be modernized or migrated individually.

Please note that modernization approaches can differ for components of the same application. For example, some components need a rebuild, while others only need a replatform to resolve the issues they are causing.

- [Choose the Right Approach to Modernize Your Legacy Systems \- 2 December 2020](https://www.gartner.com/document/code/347617?ref=dochist)

#### Have questions? Try AskGartnerBETA

Get faster answers from trusted Gartner sources with our **generative AI research assistant**.