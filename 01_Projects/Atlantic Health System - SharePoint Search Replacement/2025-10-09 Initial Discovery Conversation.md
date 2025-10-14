---
title: Atlantic Health System - SharePoint Search Replacement Initial Discovery
date: 2025-10-09
type: project
status: discovery
client: Atlantic Health System
project: SharePoint Search Replacement
deadline: 2026-07-01
tags: [project, atlantic-health, sharepoint, search, discovery, cloud-architecture, azure, aws]
stakeholders: ['IT Infrastructure Team', 'M365 Team', 'Clinical Informatics', 'Finance', 'Security/Compliance']
technologies: ['SharePoint', 'AWS OpenSearch', 'Azure AI Search', 'Copilot Studio', 'M365']
decision_factors: ['TCO', 'Multi-cloud', 'Security', 'User Experience', 'Timeline']
key_insights:
  - 'SharePoint functions as search aggregation platform, not content repository'
  - 'EOL deadline (July 2026) is forcing function'
  - 'M365 licensing already paid shifts TCO in favor of Microsoft solutions'
  - 'Multi-cloud reality (AWS + M365) creates technical and political tensions'
  - 'Interest in AI capabilities suggests desire to modernize UX beyond replacement'
open_questions_count: 10
solution_options: ['AWS OpenSearch', 'Azure AI Search', 'Copilot Studio']
priority: high
---
# Atlantic Health System - SharePoint Search Replacement
## Initial Discovery Conversation
**Date:** 2025-10-09
**Status:** Discovery / Requirements Gathering
**Decision Timeline:** Pre-July 2026 (EOL deadline)

---

## Project Context

### The Forcing Function
- Current implementation uses **on-premise SharePoint** (EOL July 2026)
- Must find replacement solution before end-of-life deadline
- This is a compliance/operational requirement, not optional

### Current Architecture
SharePoint is functioning as a **search aggregation platform**:
- **Multiple source systems** (3-5 sources)
- Content pulled into SharePoint for indexing
- Users access through simple search interface
- Not primarily used as content repository - it's the search/discovery layer

### Key Architectural Pattern
```
[Source Systems] → [Data Ingestion] → [SharePoint Index] → [Search UI] → [Users]
```

---

## Solution Options Under Consideration

### 1. AWS OpenSearch
**Rationale:**
- Atlantic Health has extensive AWS footprint
- Core systems and data likely in AWS
- Data gravity argument (keep data where it lives)

**Considerations:**
- More DIY approach (build UI, connectors, maintenance)
- Requires team with AWS expertise
- Separate infrastructure costs
- Cross-cloud identity federation complexity

### 2. Azure AI Search
**Rationale:**
- Pre-built connectors for common sources
- Semantic/vector search capabilities built-in
- Managed service (less operational overhead)
- Within Microsoft ecosystem already in use

**Considerations:**
- Cross-cloud data movement (if sources in AWS)
- Incremental cost on top of M365
- New cloud platform to manage (if AWS-heavy org)
- Security trimming built-in

### 3. Copilot Studio
**Rationale:**
- Conversational AI interface (modern UX)
- Rapid prototyping/demo-ability
- Users familiar with Microsoft tools
- Potentially included in M365 licensing

**Considerations:**
- Requires data in Microsoft ecosystem
- Less control over experience
- Newest/least mature technology
- Most vendor lock-in
- May need Azure AI Search as backend

---

## Key Decision Factors

### Total Cost of Ownership (TCO)
- **Critical insight:** Atlantic Health is current M365 user
- **Microsoft licensing already paid for** - this dramatically shifts TCO
- Question: Why is AWS OpenSearch still in running if M365 provides better TCO?

### Multi-Cloud Reality
- Extensive AWS infrastructure (core systems)
- M365 for collaboration/productivity
- Likely Azure AD/Entra for identity
- This is both technical AND political decision

### Technical Requirements (To Be Determined)
- [ ] Number and location of 3-5 source systems
- [ ] API availability from source systems
- [ ] Current data ingestion/ETL processes
- [ ] Security model (everyone searches everything vs. permission-based)
- [ ] Content types (clinical vs. administrative)
- [ ] HIPAA/PHI requirements
- [ ] Performance/scale requirements

---

## Open Questions

### Architecture & Integration
1. **Where do the 3-5 source systems live?**
   - AWS-native applications?
   - SaaS (Workday, ServiceNow, etc.)?
   - On-premise systems?
   - Mix?

2. **What's the current ingestion mechanism?**
   - Custom connectors/APIs?
   - Scheduled ETL jobs?
   - Real-time sync?
   - Third-party integration tools?

3. **Content storage pattern:**
   - Full document copies in SharePoint?
   - Metadata + links to source?
   - Index-only (no content copy)?

### Security & Identity
4. **Identity provider:**
   - Azure AD/Entra (favors Microsoft)?
   - AWS Cognito?
   - On-prem AD with federation?

5. **Search security model:**
   - Universal access?
   - Source-system permission inheritance?
   - Custom security trimming?

### User Experience
6. **Is there appetite for AI/conversational interface?**
   - Clinical staff want natural language queries?
   - Or prefer traditional ranked results?
   - Time-sensitive workflows (answer vs. documents)?

7. **Current search experience:**
   - Does the simple interface work well?
   - Users love it, tolerate it, or hate it?
   - Known pain points?

### Strategic Direction
8. **Cloud strategy for next 5 years:**
   - Double down on AWS?
   - Multi-cloud accepted?
   - Migrate toward Microsoft cloud?

9. **Why is AWS OpenSearch still being considered** if M365 TCO is better?
   - Technical team preference?
   - Data residency requirements?
   - Lock-in concerns?
   - Integration complexity?
   - Previous Microsoft experiences?

10. **What's the team skill set?**
    - AWS engineers (Terraform, CloudFormation)?
    - Microsoft admins (Azure Portal, PowerShell)?
    - Mix of both?

---

## Potential Architecture Patterns

### Option A: Microsoft-Native Stack
```
[Source Systems] → [Azure AI Search Connectors] → [Azure AI Search Index]
                 → [Copilot Studio UI] → [Users]
```
**Pros:** Leverages existing M365, integrated identity, managed service
**Cons:** Cross-cloud data movement if sources in AWS, vendor lock-in

### Option B: AWS-Native with Custom UI
```
[AWS Source Systems] → [Lambda/Custom ETL] → [OpenSearch Index]
                     → [Custom React UI + AI] → [Users]
```
**Pros:** Data gravity, AWS expertise, flexibility
**Cons:** Higher build/maintain cost, separate from M365 ecosystem

### Option C: Hybrid Approach
```
[Source Systems] → [Azure AI Search] → [Custom UI or Copilot Studio]
                                     → [OpenAI/Anthropic for AI features]
```
**Pros:** Best of both worlds, cloud-agnostic AI
**Cons:** Complexity, multiple vendors

---

## Next Steps / Information Needed

### Technical Discovery
- [ ] Map out all 3-5 source systems (name, location, API availability)
- [ ] Document current data flow and ingestion processes
- [ ] Identify security/permission requirements
- [ ] Quantify scale (documents, users, query volume)
- [ ] Review HIPAA/compliance requirements

### Financial Analysis
- [ ] Detailed TCO comparison (3-year)
  - AWS OpenSearch: infrastructure + engineering + ops
  - Azure AI Search: service costs + connectors + engineering
  - Copilot Studio: licensing delta + configuration
- [ ] Factor in data egress costs (if cross-cloud)
- [ ] Include engineering time/opportunity cost

### Stakeholder Alignment
- [ ] Who are the decision makers?
- [ ] What are their individual priorities?
  - IT infrastructure team
  - M365/end-user computing team
  - Clinical informatics
  - Finance
  - Security/compliance
- [ ] Timeline and decision process
- [ ] Risk tolerance and vendor lock-in stance

### Proof of Concept
- [ ] Define success criteria for POC
- [ ] Select 1-2 representative data sources
- [ ] Build quick prototype for each option
- [ ] User testing with clinical staff
- [ ] Performance/cost validation

---

## Key Insights from Discussion

1. **This is search aggregation**, not content management - SharePoint is the indexing engine, not the repository

2. **EOL is the forcing function** - deadline-driven decision, not performance-driven

3. **M365 licensing shifts TCO** - Microsoft solutions have built-in economic advantage

4. **Multi-cloud reality creates tension** - AWS infrastructure vs. M365 productivity suite

5. **AI capabilities are attractive** - Copilot Studio interest suggests desire to modernize UX, not just replace functionality

6. **Decision is as political as technical** - different teams have different preferences and incentives

---

## Critical Question to Answer

**What would it take to eliminate one of these three options?**

This will reveal:
- Non-negotiable requirements
- Hidden constraints
- Real decision criteria
- Political dynamics

The answer will likely point to the actual path forward.
