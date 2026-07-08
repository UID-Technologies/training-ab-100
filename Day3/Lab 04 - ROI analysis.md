## Lab 04 - ROI analysis

1. **ROI formula**

```text
ROI % = (Benefits - Total Cost) / Total Cost × 100
```

Where:

```text
Total Cost = Cost to Achieve + Cost to Maintain
```

2. **NPV formula**

```text
NPV = Rt / (1 + i)^t
```

Where:

```text
Rt = cash flow in year t
i = discount rate
t = year/time period
```

---

# Example: AI-Powered IT Support Agent ROI

## Scenario

ABC Manufacturing wants to build an **AI-powered IT Support Agent** using Copilot Studio.

The agent will answer common IT questions and reduce manual service desk tickets.

---

## Current Manual Process

| Item                         |       Value |
| ---------------------------- | ----------: |
| Tickets per month            |      10,000 |
| Avg handling time per ticket |  12 minutes |
| Support cost per hour        |        ₹600 |
| Monthly effort               | 2,000 hours |
| Monthly manual cost          |  ₹12,00,000 |

Calculation:

```text
10,000 × 12 minutes = 120,000 minutes
120,000 / 60 = 2,000 hours
2,000 × ₹600 = ₹12,00,000 per month
```

---

# AI-Powered Solution Estimate

Assume the AI agent resolves **40% tickets automatically**.

| Item              |           Value |
| ----------------- | --------------: |
| Tickets automated |     4,000/month |
| Time saved        | 800 hours/month |
| Monthly benefit   |       ₹4,80,000 |

Calculation:

```text
4,000 × 12 minutes = 48,000 minutes
48,000 / 60 = 800 hours
800 × ₹600 = ₹4,80,000 monthly benefit
```

---

# Cost of AI Solution

## Cost to Achieve

| Cost Item                     |     Amount |
| ----------------------------- | ---------: |
| Copilot Studio design & build |  ₹6,00,000 |
| Knowledge preparation         |  ₹2,00,000 |
| Integration with ITSM         |  ₹3,00,000 |
| Testing & governance          |  ₹1,00,000 |
| Total implementation cost     | ₹12,00,000 |

## Cost to Maintain

| Cost Item                | Monthly Cost |
| ------------------------ | -----------: |
| Licenses/platform        |    ₹1,00,000 |
| Model/token usage        |      ₹50,000 |
| Monitoring/support       |      ₹75,000 |
| Knowledge updates        |      ₹25,000 |
| Monthly maintenance cost |    ₹2,50,000 |

---

# Monthly ROI Calculation

```text
Monthly Benefit = ₹4,80,000
Monthly Cost to Maintain = ₹2,50,000

Net Monthly Benefit = ₹4,80,000 - ₹2,50,000
Net Monthly Benefit = ₹2,30,000
```

ROI:

```text
ROI % = (Benefits - Cost) / Cost × 100

ROI = (₹4,80,000 - ₹2,50,000) / ₹2,50,000 × 100
ROI = 92%
```

Meaning:

> For every ₹100 spent monthly on the AI solution, the organization gets ₹92 net return.

---

# Payback Period

```text
Implementation Cost = ₹12,00,000
Net Monthly Benefit = ₹2,30,000
```

```text
Payback Period = ₹12,00,000 / ₹2,30,000
Payback Period = 5.2 months
```

Meaning:

> The project recovers its initial investment in around 5 months.

---

# NPV Example for 3 Years

Assume:

```text
Annual net benefit = ₹2,30,000 × 12 = ₹27,60,000
Discount rate = 12%
Initial investment = ₹12,00,000
```

NPV:

```text
Year 1 PV = 27,60,000 / (1.12)^1 = ₹24,64,286
Year 2 PV = 27,60,000 / (1.12)^2 = ₹21,99,235
Year 3 PV = 27,60,000 / (1.12)^3 = ₹19,63,603
```

Total present value:

```text
₹24,64,286 + ₹21,99,235 + ₹19,63,603 = ₹66,27,124
```

Final NPV:

```text
NPV = ₹66,27,124 - ₹12,00,000
NPV = ₹54,27,124
```

Meaning:

> After considering the time value of money, the AI solution still creates around ₹54 lakh value over 3 years.

---

## Explanation

> ROI tells us whether the AI solution is profitable.
> Payback period tells us how quickly we recover the investment.
> NPV tells us whether the future benefits are still valuable after applying discounting.

For AI-powered business solutions, we should not calculate only token cost. We must include:

```text
Implementation cost
Licensing cost
Model/token cost
Integration cost
Data preparation cost
Security and governance cost
Monitoring cost
Maintenance cost
```

And compare that against:

```text
Time saved
Cost reduced
Productivity improved
Revenue increased
Errors reduced
Customer experience improved
Risk reduced
```
