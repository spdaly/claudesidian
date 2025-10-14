---
title: "Using TIME for Application and Product Portfolio Triage: Data From the Field"
source: "https://www.gartner.com/document-reader/document/4006458?ref=authrightrec&refval=5594859"
author:
published:
created: 2025-10-14
description: "Applications and software engineering leaders have been using Gartner’s TIME analysis to clean up their portfolios for almost two decades. Data from Gartner Consulting application portfolio optimization projects shows what leaders are finding and the remediation actions they take."
tags:
  - "clippings"
---
Applications and software engineering leaders have been using Gartner’s TIME analysis to clean up their portfolios for almost two decades. Data from Gartner Consulting application portfolio optimization projects shows what leaders are finding and the remediation actions they take.

## Overview

---

### Key Findings

- With constrained budgets and limited appetite for change, leaders require a quick and fact-based approach, working with business and finance stakeholders to identify and prioritize improvement initiatives that matter most to business and IT.
- Business engagement is a vital element of any application portfolio improvement effort, and initiatives without business input and consent usually fail.
- Too often, applications and software engineering leaders assess the portfolio once and don’t reevaluate it for years, allowing existing applications to degrade and become a burden on resources and budgets.

## Introduction

---

Applications and software engineering leaders often see their portfolios as a messy pile of hundreds (or even thousands) of applications and products. Over the years, these portfolios have deteriorated in quality and fitness. They have accumulated technical debt, such as running on out-of-date application stacks and platforms.

With budget restrictions and limited appetite for risk and change, the question becomes: “Where must we start improving our portfolio?” And the answer: “With those applications where the pressure from business, technology and cost is so high that it creates an inflection point so that both business and IT have a motivation to change.” The business view is vital to the assessment, as application spending is prioritized by business need.

The goal of the TIME model is to enable leaders to assess their application portfolio from a business, IT and cost perspective. They should then divide the portfolio into the four TIME categories (tolerate, invest, migrate, and eliminate) to classify applications by strategy (see Figure 1). The TIME model is an effective instrument to communicate to all stakeholders. It shows the portfolio’s health at a glance, and aids analysis and discussion in order to identify and prioritize opportunities for improvement.

![Visualization of application portfolio as a messy pile being examined for Business, Technical, and Cost fitness using Gartner’s four Quadrant TIME model.](https://www.gartner.com/resources/756500/756569/Figure_1_Use_TIME_to_Assess_an_Application_Portfolio_Under_Pressure.png)

Figure 1: Use TIME to Assess an Application Portfolio Under Pressure

## Analysis

---

### Triage Your Application and Product Portfolio Using the Gartner TIME Model

The goal of the application portfolio assessment is to identify and prioritize the most significant opportunities to improve the portfolio. The applications are evaluated to see how fit for purpose they are. Deficient applications may suffer from poor business fitness, technical fitness or both. Poor fitness is a risk to the business, and needs to be remediated.

Gartner’s TIME model is a key analysis tool for the assessment process. Applications are scored on a variety of business, technical and cost fitness indicators, and the sum of the scores of each type is used to position the dots on a two-by-two chart, as shown in Figure 2. The inverse of the cost fitness score is used to size the dots, making the poorly performing ones a “bigger target.”

![Two by Two with sized dots representing the business, technical, and cost fitness of each application in the portfolio.](https://www.gartner.com/resources/756500/756569/Figure_2_TIME_Categorization_of_Applications_and_Products_in_a_Portfolio.png)

Figure 2: TIME Categorization of Applications and Products in a Portfolio

Any application toward the top right is “fitter” than one toward the bottom left. The quadrants are named to indicate how applications should be viewed when making decisions about their fitness and remediation.

- **Tolerate —** the application is in good technical shape but lacking in business support, so IT would tolerate it in the portfolio until such time as the business wanted to invest in improving its business fitness.
- **Invest —** the application is in good shape, so you should invest in it when asked to add features or turn on some new functionality of a packaged application, while also keeping it technically healthy.
- **Migrate (or Modernize)** **—** The application does just what the business wants, but IT is concerned with the age and brittleness of the underlying technology. If the business wants functional improvements, IT should try to address this technical debt simultaneously by migrating the technical stack or the packaged application to current, supported technology.
- **Eliminate (or Replace) —** These applications may be in such bad shape it is not worth spending on them. If they are not needed, or the functionality is now available in a better application, they could be eliminated. If the functionality is still needed, they might need to be replaced.

In a large core system like ERP, the business fitness might vary widely by end-to-end business process or module. You may need to evaluate major modules or functional areas of the application separately from a business capability perspective to get a true picture.

The application and product portfolio assessment is also an important foundation for any application strategy. It answers the questions: “Where are we now?” and “What are the most relevant issues we need to fix in the short and long term?” The TIME model is especially helpful, as each category has its own distinct high-level strategy (see Engage the Business by Developing an Application Strategy Together).

The scoring for technical fitness, business fitness and cost is based on a combination of performance indicators. To keep this assessment as efficient as possible, the number of indicators should be limited and “just enough” to give a relevant indication of health. Gartner has defined a best practice for the process and suggested indicators for this assessment, and has implemented these into a Toolkit (see How to Assess Your Application and Product Portfolio for Business and Technical Fitness and Toolkit: Application Portfolio Business and Technical Fitness Assessment). The Toolkit is based in Microsoft Excel. It creates TIME diagrams and redundancy tables, and links applications with pace layers, business capability and organization units.

Various application portfolio tools on the market have equivalent functionality, often with quadrant-based analysis tools similar to the TIME model (see Market Guide for Application Portfolio Management Tools).

### Select a Remediation Strategy for Each TIME Quadrant

Gartner Consulting uses the TIME model in its application portfolio management (APM) engagements. It has used the model in over 140 engagements and analyzed over 24,000 applications. Figure 3 shows how those applications were distributed by TIME quadrant. These are averages over many portfolios, and your results may vary. Subsequent sections will address each in turn and describe patterns detected in the data.

![TIME quadrants labeled with percentages of application found in each.](https://www.gartner.com/resources/756500/756569/Figure_3_Typical_TIME_Distribution_Found_by_Gartner_Consulting.png)

Figure 3: Typical TIME Distribution Found by Gartner Consulting

#### Tolerate: Reengineer

Applications in the “tolerate” category have a medium-to-high technical fitness and a low-to-medium business fitness. From a risk perspective, these are not the applications in the highest need of attention in the portfolio, and are often left alone. Some characteristics of these applications include:

- They are not optimized or aligned to current business processes. The business fitness of these applications has deteriorated due to the development of new requirements, changing business context and emerging new technology.
- Their deterioration may indicate a lack of agility due to a complex technical structure that makes the application risky and expensive to change.
- If costs are acceptable and they satisfy business needs at acceptable levels of risk and quality, they will be tolerated by the business, but are not perceived by users as delivering the best support.
- Gartner Consulting found that applications in this quadrant had typically been in the environment for less than three years and scored poorly on training and usability, meaning a new round of training may improve their business fitness.
- Gartner Consulting also found that the average license spend for applications in this quadrant is 57% higher than applications in other quadrants, representing an opportunity for vendor and cost optimization.

From a portfolio perspective, these applications may be “good enough,” especially if there are applications in “migrate” and “eliminate” that need more attention. The recommendation for most organizations is to leave the applications in the “tolerate” category alone, but keep a close watch on their overall fitness.

- Investigate whether relatively low-cost training or usability improvements would change the perception and value of the application.
- Reevaluate these applications from time to time. At some point in time, the business will not tolerate the applications any longer, and will be willing to invest in improving functionality. A high cost profile will create higher urgency.

#### Invest: Innovate, Evolve

Applications in the “invest” category score medium-to-high in both technical and business fitness. The applications in this category have above-average business fitness, future potential and no issues with information quality, availability or effectiveness. Technical risk is acceptable in quality areas like recovery, security, maintainability and alignment with enterprise standards. These applications are able to keep pace with change to support dynamics and changing requirements from the business. The Gartner Consulting study found:

- Newer applications dominate in this category, with 41% being three years old or less, and another 25% being seven years old or less. If a new application does not feature in this category, then something has gone very wrong in its implementation.
- They are primarily commercial off-the-shelf (COTS) applications (52%) compared to other quadrants.
- They are more likely than applications in other quadrants to be at a stage in their life cycle where they are being developed and enhanced (44%).
- They tend to have larger user bases than applications in other quadrants, and a higher percentage of dedicated support spending (46% higher than applications in other quadrants). As a consequence, they get more resources devoted to training.

To keep these applications in good shape, you should:

- Keep these applications technically up to date so they don’t sink into the “migrate” quadrant. Keep them compliant with architecture and structured to be clearly suitable for further investment, integration and reuse.
- Look to these systems as future strategic platforms, and identify ways to further improve their agility and efficiency.
- Manage these applications as important business assets. Stay engaged with the business to track changing business needs and evolve the application to meet them.
- Keep a close watch on the agility of these applications to see if they can keep pace with change. If they can’t, the applications will not be able to support new business requirements in time, and business fitness will quickly deteriorate. Exploit agile, DevOps and product-oriented delivery models to improve the agility of the applications.
- Look to improve the efficiency of operations and maintenance if an application has a high cost profile. If costs are not acceptable to the business, explore ways to standardize and eliminate customizations to lower the application’s footprint.

#### Migrate: Modernize

Applications in this category score highly in business fitness, but have issues in the technical domain. They pose a risk or have quality issues in areas like stability, security, maintainability and supportability. This can be due to the use of old or unsupported technology, a lack of skilled workers, high complexity or high technical debt. These applications are valuable business assets and need immediate attention in the form of technical remediation or migration programs to preserve business value and reduce risk.

The Gartner Consulting study found:

- Older applications dominate in this category, with 50% being eight years old or more, and 24% being 12 years old or more.
- Most (82%) are custom applications, primarily managed by internal IT resources.
- The technical and IT debt of these applications is high, as evidenced by a higher percentage of databases and operating systems nearing end-of-life.
- Budget for application support is typically lacking in this quadrant, with a historical trend of 40% less spend for routine maintenance support compared to other quadrants.
- Despite the constraints listed above, the study found that these are applications the business uses a lot, evidenced by the highest utilization rates across the portfolio, with “constant system interactions and information access” requirements.

Replacing applications in this quadrant may not be the best option, as it is usually better to preserve the business fitness and value of the applications and avoid the disruption for the business to adopt something new. To improve these applications, you should:

- Use the TIME analysis to convince the business that, when spending money to improve functionality, the technical stack and/or the packaged application should be updated to a current, supported release.
- Initiatives in this category are largely aimed at reducing risk and cost. A detailed, bottom-up analysis of application dependencies needs to be undertaken, along with an assessment of potential consolidation, conversion, modernization and migration techniques.
- In companies undertaking a cloud migration strategy, the applications in this category may be good candidates, as the migration process will require the same types of work to remediate technical debt.

Applications and software engineering leaders have a choice of modernization approaches that improve particular aspects of technical fitness. These include rehost, replatform, refactor and rearchitect. Choose the modernization approach that tackles the root cause of the problem (see Choose the Right Approach to Modernize Your Legacy Systems).

#### Eliminate: Replace, Consolidate

Applications in this category are the “rotten apples” in the portfolio. Low business and technical fitness beg the question: “Why do we keep these applications alive, especially if they have a high cost profile?” While there is high pressure to decommission them to save money, it isn’t often that easy. The Gartner Consulting study found:

- Applications in this quadrant are typically custom-built legacy applications that have been in the portfolio for eight years or more.
- The drivers for poor technical fitness are integration challenges and extensibility limitations.
- Business fitness constraints are driven by inadequate training and poor overall usability.
- One in four of these applications is duplicative of other applications.

Eliminating applications might seem a simple exercise, but this is rarely the case. Business users almost always still rely on the applications’ functions and data, so they can’t simply be shut off. In addition, the data may need to be retained for regulatory and analysis purpose s. But there can be benefits to eliminating these applications as well. The most obvious benefits are potential savings in costs and resources to manage these applications, as well as contribution to any technical debt reduction program. Eliminating these applications takes their technical debt with them, without the need for any separate remediation plans.

- Find out if anyone is still using the application. If not, ask to decommission it.
- Look at the duplicative applications and determine whether their work can be consolidated into another application in the portfolio. As discussed in the next section, you will need to create a business case that both covers the costs and provides an incentive for the business groups to change.
- Make IT and business stakeholders aware of the risks and issues associated with applications in areas like security, compliance and vendor support. These will pose a business risk, which can be a decisive factor to motivate all stakeholders to take action.
- Evaluate whether upgrading the application to a more modern technical stack and improving the user experience would be a cost-effective solution.
- Challenge any request for functional enhancements with a recommendation to replace the application instead.

Create the role of “application undertaker” as an ongoing discipline to decommission applications and deal with data retention in an efficient way. Standards covering processes, policies and tools will make the process efficient and compliant (see Decommissioning Applications: The Emerging Role of the Application Undertaker and There Are Many Options for Data Retention After Application Decommissioning).

### Engage Business Stakeholders to Identify Business Cases

Application spending is always driven by business priorities. IT needs the consent of, and support from, the business to make any meaningful change to the application portfolio. Applications and software engineering leaders and business stakeholders should start by building a sense of joint ownership and making a joint decision (see also In Application Rationalization, the Number of Applications Is Irrelevant).

Using the TIME model in your discussions with business stakeholders helps set funding priorities, since improvements to the existing portfolio compete for budget with new applications. With all cards on the table, an informed business decision can be made to invest in improving the applications’ assets.

A TIME analysis is created for each business domain and its key stakeholder. For example, an analysis of all finance applications will aid a discussion with the VP of finance on business priorities: “These are your applications. You are dependent on these assets and this is their health. Can we talk about how to improve them?”

Making major changes to business applications is expensive. An important part of the discussion is to determine the required business outcomes. A business outcome is a measurable improvement in a business capability through change to the process (including applications) that usually has a financial benefit. It is also the benefit side of the business case. Matched with the estimated cost, each proposed action can be compared to determine what to act on.

### Address “Future Legacy” by Assessing the Portfolio Regularly

APM must be an ongoing discipline (see Managing a Portfolio of Applications Demands More Than Application Portfolio Management). Applications age, while their business and technical fitness change over time, as do delivery models (e.g., cloud, XaaS). Improvement initiatives will reshape the portfolio. Changes in the business context, vendor product strategies, availability of skills and the introduction of new technology will impact the health of the portfolio. As a result, applications will move around in the TIME model, shifting between categories.

Gartner Consulting data shows a wide range of ages for applications in each quadrant (see Table 1). As you might expect, older applications are more likely to fall in the low technical fitness quadrants of “migrate” and “eliminate.” But a sizable number of younger applications are also in those quadrants. This indicates that applications can age rapidly as technology and business needs evolve.

### Table 1: Distribution of Age of Applications in Gartner Consulting Application Portfolio Engagements

<table><thead><tr><th colspan="1"></th><th colspan="6"><span><p><span><strong>Age of Application (years)</strong></span></p></span></th></tr></thead><tbody><tr><td colspan="1"><p><span><strong>TIME Quadrant</strong></span></p></td><td colspan="1"><p><span><strong>0 to 3</strong></span></p></td><td colspan="1"><p><span><strong>4 to 7</strong></span></p></td><td colspan="1"><p><span><strong>8 to 11</strong></span></p></td><td colspan="1"><p><span><strong>12 to 19</strong></span></p></td><td colspan="1"><p><span><strong>20+</strong></span></p></td><td colspan="1"><p><span><strong>Overall Quadrant</strong></span></p></td></tr><tr><td colspan="1"><p><span><strong>Tolerate</strong></span></p></td><td colspan="1"><p><span><span>38%</span></span></p></td><td colspan="1"><p><span><span>32%</span></span></p></td><td colspan="1"><p><span><span>18%</span></span></p></td><td colspan="1"><p><span><span>11%</span></span></p></td><td colspan="1"><p><span><span>2%</span></span></p></td><td colspan="1"><p><span><span>16%</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Invest</strong></span></p></td><td colspan="1"><p><span><span>41%</span></span></p></td><td colspan="1"><p><span><span>28%</span></span></p></td><td colspan="1"><p><span><span>17%</span></span></p></td><td colspan="1"><p><span><span>11%</span></span></p></td><td colspan="1"><p><span><span>3%</span></span></p></td><td colspan="1"><p><span><span>44%</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Migrate</strong></span></p></td><td colspan="1"><p><span><span>22%</span></span></p></td><td colspan="1"><p><span><span>29%</span></span></p></td><td colspan="1"><p><span><span>26%</span></span></p></td><td colspan="1"><p><span><span>19%</span></span></p></td><td colspan="1"><p><span><span>5%</span></span></p></td><td colspan="1"><p><span><span>22%</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Eliminate</strong></span></p></td><td colspan="1"><p><span><span>21%</span></span></p></td><td colspan="1"><p><span><span>28%</span></span></p></td><td colspan="1"><p><span><span>23%</span></span></p></td><td colspan="1"><p><span><span>23%</span></span></p></td><td colspan="1"><p><span><span>4%</span></span></p></td><td colspan="1"><p><span><span>14%</span></span></p></td></tr><tr><td colspan="1"><p><span><strong>Overall Age</strong></span></p></td><td colspan="1"><p><span><strong>33%</strong></span></p></td><td colspan="1"><p><span><strong>29%</strong></span></p></td><td colspan="1"><p><span><strong>21%</strong></span></p></td><td colspan="1"><p><span><strong>15%</strong></span></p></td><td colspan="1"><p><span><strong>3%</strong></span></p></td><td colspan="1"></td></tr></tbody><tbody><tr><td colspan="2"><p><span><span>n = 12,811</span></span></p></td></tr></tbody></table>

Source: Gartner (September 2021)

Assess the application portfolio on a regular basis. Preserve the value of the process and inventory by refreshing the data and revisiting assumptions. Revisit reviews, not only when internal factors change, but also when business conditions or other external events impact the costs, risks or fitness of the elements of the portfolio. These assessments should be revisited on at least a yearly basis, and your portfolio data updated to close previous gaps or address new applications quarterly. This enables a faster response to changing circumstances, and so should be preferred for domains where the business and/or technology are changing rapidly.

Regular assessments will show to all stakeholders the changes and progress made in the portfolio, and will prove the value of the APM process. Assessments will also help to retain awareness and a sense of ownership among all stakeholders, making them better asset owners and managers. In a continuously managed portfolio, the shifts between categories can be predicted and managed. The visibility of application costs and risks will also generally improve the credibility of IT’s plans.

## Additional Research Contribution

---

Eric Klintberg of Gartner Consulting contributed portfolio statistics and analysis to this research.

## Evidence

---

The dataset is derived from 143 application portfolio management projects conducted by Gartner Consulting from 2007 through 2021 across multiple industries, including banking, energy & utilities, education, healthcare, technology, insurance, manufacturing, pharmaceutical, public sector and retail.

Best practices and analysis are based on over 625 client interactions since the beginning of 2019.

- [Use TIME to Engage the Business for Application and Product Portfolio Triage \- 1 September 2020](https://www.gartner.com/document/code/382785?ref=dochist)

#### Have questions? Try AskGartnerBETA

Get faster answers from trusted Gartner sources with our **generative AI research assistant**.