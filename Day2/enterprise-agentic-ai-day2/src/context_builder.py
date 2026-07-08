def build_enterprise_context(role, task, business_context, constraints, examples, retrieved_context):
    context = f"""
ROLE:
{role}

TASK:
{task}

BUSINESS CONTEXT:
{business_context}

CONSTRAINTS:
{constraints}

EXAMPLES:
{examples}

RETRIEVED ENTERPRISE CONTEXT:
{retrieved_context}

INSTRUCTIONS:
- Think like a senior enterprise architect.
- Ground recommendations in retrieved policy context.
- Identify risks and mandatory controls.
- Avoid generic answers.
- Return structured output.
"""
    return context.strip()
