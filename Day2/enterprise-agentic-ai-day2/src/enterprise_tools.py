import json
from datetime import datetime

from src.trace_logger import log_metric, log_trace


def check_credit_score(legal_name, country):
    base_score = 55
    if "global" in legal_name.lower():
        base_score += 20
    if country.upper() in {"US", "DE", "SG", "SE"}:
        base_score += 10

    return {
        "provider": "MockDandB",
        "legal_name": legal_name,
        "country": country,
        "credit_score": min(max(base_score, 10), 95),
        "payment_behavior": "Stable" if base_score >= 60 else "Watchlist",
        "checked_at": datetime.now().isoformat(),
    }


def screen_sanctions_list(legal_name, country):
    flagged_keywords = ["shadow", "restricted", "sanction"]
    is_flagged = any(keyword in legal_name.lower() for keyword in flagged_keywords)

    return {
        "provider": "MockSanctionsAPI",
        "legal_name": legal_name,
        "country": country,
        "match_found": is_flagged,
        "risk_level": "HIGH" if is_flagged else "LOW",
        "lists_checked": ["OFAC", "EU_SANCTIONS", "UN_CONSOLIDATED"],
        "checked_at": datetime.now().isoformat(),
    }


def register_supplier_in_erp(supplier_id, legal_name, category, annual_spend_usd):
    return {
        "provider": "MockSAPAriba",
        "supplier_id": supplier_id,
        "legal_name": legal_name,
        "category": category,
        "annual_spend_usd": annual_spend_usd,
        "erp_vendor_code": f"VND-{supplier_id[-4:]}",
        "status": "REGISTERED",
        "registered_at": datetime.now().isoformat(),
    }


def calculate_risk_score(credit_score, sanctions_match, spend_usd):
    score = 100 - credit_score
    if sanctions_match:
        score += 40
    if spend_usd >= 500000:
        score += 10

    score = min(max(score, 5), 100)

    return {
        "risk_score": score,
        "risk_band": "HIGH" if score >= 65 else "MEDIUM" if score >= 40 else "LOW",
        "factors": {
            "credit_score": credit_score,
            "sanctions_match": sanctions_match,
            "annual_spend_usd": spend_usd,
        },
    }


TOOL_DEFINITIONS = [
    {
        "name": "check_credit_score",
        "description": "Call external credit bureau API to retrieve supplier credit score.",
        "parameters": {
            "type": "object",
            "properties": {
                "legal_name": {"type": "string"},
                "country": {"type": "string"},
            },
            "required": ["legal_name", "country"],
        },
    },
    {
        "name": "screen_sanctions_list",
        "description": "Screen supplier against global sanctions and restricted entity lists.",
        "parameters": {
            "type": "object",
            "properties": {
                "legal_name": {"type": "string"},
                "country": {"type": "string"},
            },
            "required": ["legal_name", "country"],
        },
    },
    {
        "name": "register_supplier_in_erp",
        "description": "Register approved supplier in ERP procurement system.",
        "parameters": {
            "type": "object",
            "properties": {
                "supplier_id": {"type": "string"},
                "legal_name": {"type": "string"},
                "category": {"type": "string"},
                "annual_spend_usd": {"type": "number"},
            },
            "required": ["supplier_id", "legal_name", "category", "annual_spend_usd"],
        },
    },
    {
        "name": "calculate_risk_score",
        "description": "Compute onboarding risk score from due diligence signals.",
        "parameters": {
            "type": "object",
            "properties": {
                "credit_score": {"type": "integer"},
                "sanctions_match": {"type": "boolean"},
                "spend_usd": {"type": "number"},
            },
            "required": ["credit_score", "sanctions_match", "spend_usd"],
        },
    },
]


def execute_tool(function_name, arguments):
    if function_name == "check_credit_score":
        return check_credit_score(**arguments)
    if function_name == "screen_sanctions_list":
        return screen_sanctions_list(**arguments)
    if function_name == "register_supplier_in_erp":
        return register_supplier_in_erp(**arguments)
    if function_name == "calculate_risk_score":
        return calculate_risk_score(**arguments)

    return {"error": f"Unknown tool: {function_name}"}


def execute_tool_with_trace(function_name, arguments, feature="tool_calling"):
    log_trace(feature, "ToolAgent", "tool_call_started", "SUCCESS", f"{function_name}({arguments})")

    try:
        result = execute_tool(function_name, arguments)
        payload = json.dumps(result)
        log_trace(feature, "ToolAgent", "tool_call_completed", "SUCCESS", payload[:500])
        log_metric(feature, "tool_calls_total", 1, function_name)
        return result
    except Exception as exc:
        log_trace(feature, "ToolAgent", "tool_call_failed", "FAILED", str(exc))
        log_metric(feature, "tool_call_errors", 1, function_name)
        raise
