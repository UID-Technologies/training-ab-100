The previous case study started with **"Client wants an AI solution."**

In reality, **clients almost never ask for AI**.

They come with a business problem.

An architect has to discover where AI fits.


---

# Case Study 2 – Global Healthcare Provider

## Theme

**Design an AI-powered Patient Care Coordination Platform**

This case study is intentionally different from Procurement.

Here the architect is solving an **operational problem**, not a knowledge-search problem.

The emphasis is on:

* Process redesign
* Human-in-the-loop
* Multi-agent orchestration
* Responsible AI
* Security
* Healthcare compliance
* Real-time integrations
* Executive decision making

This aligns extremely well with AB-100 planning, designing and deploying objectives. 

---

# Scene 1 – Client Meeting

You enter a discovery workshop.

The CIO says:

> "Our hospitals are growing rapidly. Every patient interacts with multiple departments, and our staff spends too much time coordinating care instead of delivering care. We don't know if AI can help, but we want to improve patient experience."

Notice something?

Nobody mentioned:

* Copilot
* Azure AI
* Agents
* Chatbots

This is exactly how enterprise engagements begin.

---

# Step 1 — Resist Jumping to Technology

Many architects immediately say:

> Let's build a Copilot.

Wrong.

Instead ask:

> Tell me what happens from the moment a patient arrives.

---

# Step 2 — Discover the Business Process

The hospital explains.

```text
Patient arrives

↓

Reception

↓

Registration

↓

Insurance Verification

↓

Doctor Consultation

↓

Lab Tests

↓

Radiology

↓

Diagnosis

↓

Prescription

↓

Billing

↓

Discharge

↓

Follow-up
```

Now everyone in class understands the business.

---

# Step 3 — Start Asking Questions

Architect thinking:

Who are the users?

Receptionist

Doctor

Nurse

Radiologist

Lab Technician

Insurance Team

Billing Team

Patient

Hospital Administrator

Each has different goals.

---

## Discussion

Ask participants:

> Should every user receive the same AI assistant?

Expected answer:

No.

Different roles require different capabilities and permissions.

---

# Step 4 — Identify Pain Points

Now keep asking "Why?"

Reception:

> Patients wait 25 minutes.

Why?

Manual registration.

Insurance verification.

Searching previous records.

---

Doctor:

> I spend 40% of my consultation reading patient history.

---

Nurse:

> We call patients to remind them about medication.

---

Lab:

> Reports are uploaded manually.

---

Billing:

> Insurance approvals are delayed.

---

Administrator:

> I cannot identify bottlenecks quickly.

---

Architect writes these on the board.

---

# Step 5 — Categorize the Problems

Teach participants to classify rather than solve immediately.

| Business Problem         | AI          | Automation | Human  |
| ------------------------ | ----------- | ---------- | ------ |
| Registration             | Partial     | Yes        | Yes    |
| Insurance Verification   | Partial     | Yes        | Yes    |
| Patient History Summary  | Yes         | No         | No     |
| Medication Reminder      | Yes         | Yes        | No     |
| Diagnosis                | Assist only | No         | Doctor |
| Appointment Scheduling   | Yes         | Yes        | No     |
| Insurance Approval       | Partial     | Yes        | Human  |
| Treatment Recommendation | Assist only | No         | Doctor |

Now participants realize AI is only one part of the solution.

---

# Step 6 — Define Success Criteria

Architect asks:

How will we know if the project is successful?

The client answers:

Reduce patient waiting time by 30%.

Reduce administrative work by 40%.

Increase doctor consultation time.

Improve patient satisfaction.

Reduce billing delays.

Increase first-time insurance approval.

These become measurable KPIs.

---

# Step 7 — Understand the Data Landscape

Draw the current systems.

```text
Electronic Medical Record

Hospital Information System

Laboratory System

Radiology System

Insurance Portal

Microsoft Teams

SharePoint

Power BI

Dataverse

Legacy SQL

Medical Devices
```

Ask:

Which systems contain structured data?

Which contain documents?

Which provide APIs?

Which are real-time?

---

# Step 8 — Data Classification

Architect creates a data inventory.

| Data                 | Type       | Sensitivity | AI Grounding?          |
| -------------------- | ---------- | ----------- | ---------------------- |
| Patient demographics | Structured | High        | Yes                    |
| Medical history      | Structured | Critical    | Yes                    |
| MRI images           | Binary     | Critical    | No (specialized model) |
| Lab reports          | PDF        | High        | Yes                    |
| Clinical guidelines  | Documents  | Medium      | Yes                    |
| Insurance policies   | Documents  | Medium      | Yes                    |
| Billing              | Structured | High        | Limited                |

Now the discussion shifts to governance.

---

# Step 9 — Should Everything Be AI?

Architect asks:

Should AI make medical diagnoses?

The room usually says "No."

Excellent.

Architect writes:

```text
AI should assist.

Doctors decide.
```

This introduces Responsible AI.

---

# Step 10 — Discover AI Opportunities

Rather than creating one large chatbot, identify focused assistants.

Possible assistants:

Patient Assistant

Doctor Assistant

Nurse Assistant

Insurance Assistant

Billing Assistant

Administrator Assistant

Now ask:

Should these be independent?

Or should they collaborate?

---

# Step 11 — Introduce Multi-Agent Thinking

Instead of one intelligent agent:

```text
Patient

↓

Care Coordinator Agent

↓

Planner Agent

↓

--------------------------------

Patient History Agent

Insurance Agent

Scheduling Agent

Medication Agent

Lab Agent

Billing Agent

Compliance Agent

--------------------------------

↓

Doctor
```

Planner decides who should participate.

Workers complete specialized tasks.

---

# Step 12 — Human-in-the-Loop

Architect asks:

When must AI stop and request approval?

Examples:

High-risk medication

Insurance rejection

Critical diagnosis

Patient discharge

Consent required

Unexpected symptoms

Teach participants to define approval gates.

---

# Step 13 — Technology Selection Workshop

Now technology finally enters the discussion.

Ask:

Should we use Microsoft 365 Copilot?

Participants discuss.

Maybe for productivity.

Should we use Copilot Studio?

Yes, for workflow orchestration.

Should we use Azure AI Foundry?

Yes, for advanced reasoning and model evaluation.

Should we use Power Automate?

Yes, for approvals and notifications.

Should we use Azure AI Search?

Yes, for clinical guidelines and policies.

The class now understands *why* each service exists.

---

# Step 14 — Security Architecture

Now change perspective.

Imagine you are the hospital's CISO.

Questions:

Can AI expose another patient's records?

How is patient identity verified?

Should doctors and nurses see the same data?

Can prompts leak sensitive information?

How do we audit AI recommendations?

What if AI hallucinates?

Should conversations be retained?

Can AI access deleted records?

This becomes a governance discussion instead of a technology discussion.

---

# Step 15 — Responsible AI Review

Discuss:

Should AI explain recommendations?

Should users know AI generated the summary?

Should confidence scores be displayed?

How do we detect hallucinations?

How do we measure bias?

Should AI answer beyond approved medical guidelines?

---

# Step 16 — Deployment Strategy

Architect asks:

Should we release to every hospital?

Probably not.

Suggested rollout:

```text
Hospital A

↓

Pilot

↓

Collect Feedback

↓

Improve Prompts

↓

Improve Agents

↓

Regional Rollout

↓

Global Rollout
```

Participants learn change management.

---

# Step 17 — Monitoring Strategy

Ask:

What should we monitor?

Examples:

Doctor adoption

Average response time

Patient satisfaction

Hallucination rate

Escalation rate

Agent failures

Insurance approval improvement

Waiting time reduction

Model cost

Prompt success rate

Grounding accuracy

---

# Step 18 — ROI Analysis

Current state:

* 20 hospitals
* 500 doctors
* Each doctor spends 1 hour/day reviewing records
* Average loaded cost: ₹2,000/hour

Current annual cost:

```text
500 × 1 × ₹2,000 × 250 days

= ₹25 crore/year
```

If AI saves 30 minutes/day:

```text
Savings ≈ ₹12.5 crore/year
```

If the AI platform costs ₹2 crore annually:

```text
Net Benefit = ₹10.5 crore/year
```

Now participants understand that architects justify investment with business outcomes, not technical features.

---

# Step 19 — Final Enterprise Architecture

```text
Patients / Doctors / Nurses
              │
              ▼
        Microsoft Teams
              │
              ▼
     Copilot Studio Front Door
              │
              ▼
        Care Coordinator Agent
              │
      Planner / Orchestrator
              │
 ┌────────────┼────────────┐
 │            │            │
 ▼            ▼            ▼
Patient   Insurance   Scheduling
History      Agent        Agent
 Agent
 │            │            │
 ▼            ▼            ▼
EMR      Insurance API   Calendar
 │
 ▼
Lab Agent ─ Radiology Agent ─ Billing Agent ─ Compliance Agent
              │
              ▼
      Azure AI Foundry
              │
              ▼
 Azure AI Search + SharePoint
              │
              ▼
 Governance • Entra ID • Audit • Monitoring • Power BI
```

---
