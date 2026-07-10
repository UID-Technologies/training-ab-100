# Case Study: Enterprise Procurement AI Assistant

## 1. Business Scenario

**Company:** Contoso Manufacturing
**Industry:** Global manufacturing
**Employees:** 80,000+
**Regions:** India, Europe, US, Middle East
**Current Platforms:**

* Microsoft 365
* Teams
* SharePoint
* Dynamics 365 Finance
* SAP Procurement
* Power Platform
* ServiceNow
* Azure

## Business Problem

Procurement teams are slow because employees struggle with:

* Finding procurement policies
* Selecting approved vendors
* Creating purchase requests
* Getting approvals
* Checking budget availability
* Validating compliance
* Tracking purchase order status
* Handling invoice exceptions

The client wants an **AI-powered procurement assistant** available inside Microsoft Teams.

---

# 2. Target Solution

Create an enterprise-grade **Procurement AI Assistant** that can:

* Answer procurement policy questions
* Search approved vendors
* Help create purchase requests
* Validate budget
* Check compliance
* Trigger approval workflow
* Track purchase orders
* Escalate risky cases to humans
* Provide audit trail
* Monitor usage, quality, and cost

---

# 3. Architect Thinking Approach

## Step 1: Understand Business Process

Before selecting technology, understand the current procurement lifecycle.

```text
Employee Need
    ↓
Search Policy
    ↓
Select Vendor
    ↓
Create Purchase Request
    ↓
Manager Approval
    ↓
Finance Budget Check
    ↓
Procurement Review
    ↓
Purchase Order
    ↓
Goods Receipt
    ↓
Invoice Processing
    ↓
Payment
```

Architect should ask:

* Who creates purchase requests?
* Which systems store procurement data?
* Which approvals are manual?
* Which decisions require compliance?
* Which tasks are repetitive?
* Which data is sensitive?
* Which users need access?
* What is the expected business outcome?

---

# 4. Identify AI Opportunities

| Area                      | AI Opportunity                       | Recommended Approach          |
| ------------------------- | ------------------------------------ | ----------------------------- |
| Policy search             | Employees ask policy questions       | RAG with SharePoint knowledge |
| Vendor selection          | Suggest approved vendors             | Agent + ERP/Dataverse lookup  |
| Purchase request creation | Generate request draft               | Copilot Studio action         |
| Budget check              | Validate available budget            | API/tool calling              |
| Compliance check          | Detect policy violations             | Compliance agent              |
| Approval                  | Route to manager/finance             | Power Automate                |
| PO tracking               | Answer status queries                | ERP connector/API             |
| Invoice exception         | Summarize issue and recommend action | Human-in-the-loop             |

---

# 5. Decide Build vs Buy vs Extend

## Option 1: Use Microsoft 365 Copilot Only

Good for:

* Searching documents
* Summarizing content
* Productivity tasks

Limitations:

* Limited custom business workflow
* Limited ERP process orchestration
* Not ideal for structured approval workflow

## Option 2: Use Copilot Studio

Good for:

* Creating business agents
* Connecting to knowledge
* Creating topics
* Adding actions
* Publishing to Teams
* Human workflow integration

## Option 3: Use Azure AI Foundry

Good for:

* Advanced model orchestration
* Custom agents
* Model routing
* Evaluation
* Custom RAG
* Advanced multi-agent design

## Final Decision

Use a hybrid approach:

```text
Microsoft Teams
    ↓
Copilot Studio Agent
    ↓
Power Automate Actions
    ↓
Dynamics 365 / SAP APIs
    ↓
Azure AI Foundry for advanced reasoning
    ↓
Azure AI Search for enterprise knowledge
    ↓
Power BI / Monitor for telemetry
```

---

# 6. High-Level Architecture

```text
User in Teams
    ↓
Procurement Copilot Agent
    ↓
Intent Detection
    ↓
Planner Agent
    ↓
------------------------------------------------
| Policy Agent       → SharePoint + AI Search   |
| Vendor Agent       → SAP / Dynamics / Dataverse |
| Budget Agent       → Dynamics 365 Finance     |
| Compliance Agent   → Policy rules + RAI checks |
| Approval Agent     → Power Automate           |
| Tracking Agent     → SAP / ERP APIs           |
------------------------------------------------
    ↓
Response Validator
    ↓
Human Approval if Required
    ↓
Final Response to User
    ↓
Telemetry + Audit + Cost Logging
```

---

# 7. Agent Design

## 1. Planner Agent

Responsible for:

* Understanding user intent
* Breaking the request into tasks
* Selecting the right worker agent
* Deciding if human approval is needed

Example:

User asks:

```text
Can I buy 25 laptops from Vendor X under the IT procurement policy?
```

Planner breaks it into:

```text
1. Check IT procurement policy
2. Validate Vendor X approval status
3. Check budget
4. Check compliance
5. Recommend next step
```

---

## 2. Policy Agent

Uses:

* SharePoint policies
* Procurement SOPs
* Vendor onboarding rules
* Contract documents

Technology:

* Copilot Studio knowledge source
* Azure AI Search
* RAG grounding

---

## 3. Vendor Agent

Uses:

* Approved vendor list
* SAP vendor master
* Dynamics supplier records
* Risk score
* Contract status

---

## 4. Budget Agent

Uses:

* Dynamics 365 Finance
* Cost center
* Budget availability
* Approval limits

---

## 5. Compliance Agent

Checks:

* Procurement threshold
* Vendor risk
* Data residency
* Contract validity
* Approval matrix
* Sensitive category rules

---

## 6. Approval Agent

Uses:

* Power Automate
* Teams adaptive card
* Manager approval
* Finance approval
* Procurement approval

---

# 8. Data and Knowledge Strategy

## Structured Data

| Data             | Source               |
| ---------------- | -------------------- |
| Vendor master    | SAP / Dynamics       |
| Budget           | Dynamics 365 Finance |
| Purchase orders  | ERP                  |
| Approval matrix  | Dataverse            |
| Employee profile | Entra ID / HR system |

## Unstructured Data

| Data                  | Source            |
| --------------------- | ----------------- |
| Procurement policy    | SharePoint        |
| Vendor contract       | SharePoint / Blob |
| SOP documents         | SharePoint        |
| Compliance guidelines | SharePoint        |

## Knowledge Design

```text
SharePoint Documents
    ↓
Document Chunking
    ↓
Embeddings
    ↓
Azure AI Search
    ↓
RAG Grounding
    ↓
Agent Response
```

---

# 9. Security Design

Architect must consider:

## Identity

* Microsoft Entra ID
* Role-based access control
* Conditional access
* MFA

## Data Access

* User should only see allowed procurement data
* Role-based grounding
* No cross-region data leakage
* No access to confidential contracts unless permitted

## Prompt Security

* Prompt injection detection
* Grounding validation
* Sensitive data filtering
* Response moderation

## Audit

Track:

* User question
* Agent used
* Data source accessed
* API called
* Model used
* Approval status
* Final response
* Cost

---

# 10. Governance Design

Create governance for:

* Prompt library
* Prompt versioning
* Agent publishing
* Knowledge source updates
* Model selection
* Responsible AI checks
* Human review
* Change approval
* Environment promotion

Governance model:

```text
AI Center of Excellence
    ↓
Architecture Review Board
    ↓
Security Review
    ↓
Responsible AI Review
    ↓
Business Owner Approval
    ↓
Production Release
```

---

# 11. ALM Strategy

Use separate environments:

```text
Development
    ↓
Test / UAT
    ↓
Pre-Production
    ↓
Production
```

For Copilot Studio:

* Export solution
* Use Power Platform pipelines
* Store configurations
* Manage environment variables
* Version actions
* Test prompts
* Validate knowledge sources

For Azure AI Foundry:

* Version prompts
* Version models
* Version evaluations
* Version indexes
* Track deployments

---

# 12. Monitoring and Observability

Monitor:

| Metric                | Purpose          |
| --------------------- | ---------------- |
| Total conversations   | Adoption         |
| Deflection rate       | Productivity     |
| Escalation rate       | Human dependency |
| Average response time | Performance      |
| Failed actions        | Reliability      |
| Cost per request      | FinOps           |
| Token usage           | Cost control     |
| User feedback         | Quality          |
| Hallucination rate    | Trust            |
| Approval cycle time   | Business impact  |

Use:

* Copilot Studio analytics
* Power Platform admin center
* Azure Monitor
* Application Insights
* Power BI dashboard

---

# 13. Model Routing Strategy

Do not use the most expensive model for every request.

```text
FAQ / Simple policy question
    → Small model

Document summarization
    → Medium model

Complex procurement reasoning
    → Advanced model

High-risk compliance decision
    → Advanced model + human approval
```

Example:

| Request Type      | Model                 |
| ----------------- | --------------------- |
| Simple FAQ        | GPT-4o mini           |
| Policy summary    | GPT-4o mini           |
| Complex reasoning | GPT-4o                |
| Risk/compliance   | GPT-4o + human review |
| Classification    | Small/fast model      |

---

# 14. Human-in-the-Loop

Human approval required when:

* Purchase value exceeds threshold
* Vendor is high risk
* Policy conflict exists
* Budget is insufficient
* Contract is expired
* Compliance rule is violated
* AI confidence is low

Workflow:

```text
AI Recommendation
    ↓
Risk Score
    ↓
Approval Required?
    ↓
Teams Adaptive Card
    ↓
Manager / Finance / Procurement Decision
    ↓
Audit Log
    ↓
Final Response
```

---

# 15. ROI Calculation

## Current State

Assume:

* 5,000 procurement users
* Each spends 30 minutes/day searching or following up
* Average cost: ₹800/hour

Daily loss:

```text
5,000 × 0.5 × ₹800 = ₹20,00,000/day
```

Annual loss:

```text
₹20,00,000 × 220 working days = ₹44 crore/year
```

## AI Solution Cost

Estimated annual cost:

* Copilot Studio licenses
* Azure AI usage
* Azure AI Search
* Power Automate
* Implementation
* Support

Example:

```text
Total estimated cost: ₹2 crore/year
```

## ROI

```text
Benefit = ₹44 crore
Cost = ₹2 crore

ROI = ((44 - 2) / 2) × 100
ROI = 2100%
```

---

# 16. Final Solution Blueprint

```text
Microsoft Teams
    ↓
Copilot Studio Procurement Agent
    ↓
Planner Agent
    ↓
Task Agents
    ├── Policy Agent
    ├── Vendor Agent
    ├── Budget Agent
    ├── Compliance Agent
    ├── Approval Agent
    └── Tracking Agent
    ↓
Power Automate
    ↓
Dynamics 365 Finance / SAP / Dataverse
    ↓
Azure AI Search + SharePoint
    ↓
Azure AI Foundry
    ↓
Responsible AI + Security Layer
    ↓
Monitoring + Audit + Cost Dashboard
```

---


# 19. Conclusion

The important learning is:

```text
A senior AI architect does not start with Copilot Studio or Azure AI Foundry.

A senior AI architect starts with:

Business Process
    ↓
Pain Points
    ↓
AI Opportunity
    ↓
Data Availability
    ↓
Security
    ↓
Integration
    ↓
Governance
    ↓
ROI
    ↓
Technology Selection
    ↓
Architecture
    ↓
Deployment
    ↓
Monitoring
```

That is the AB-100 architect mindset.
