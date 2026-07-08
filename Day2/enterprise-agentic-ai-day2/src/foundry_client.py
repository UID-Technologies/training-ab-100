import json

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    AssistantMessage,
    ChatCompletionsToolDefinition,
    FunctionDefinition,
    SystemMessage,
    ToolMessage,
    UserMessage,
)
from azure.core.credentials import AzureKeyCredential

from src.config import AZURE_AI_ENDPOINT, AZURE_AI_KEY, PRIMARY_MODEL
from src.cost_tracker import log_cost


client = ChatCompletionsClient(
    endpoint=AZURE_AI_ENDPOINT,
    credential=AzureKeyCredential(AZURE_AI_KEY),
)


def ask_ai(
    system_prompt,
    user_prompt,
    model=None,
    temperature=0.2,
    feature="general",
):
    selected_model = model or PRIMARY_MODEL

    response = client.complete(
        model=selected_model,
        messages=[
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt),
        ],
        temperature=temperature,
    )

    answer = response.choices[0].message.content

    usage = getattr(response, "usage", None)
    input_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
    output_tokens = getattr(usage, "completion_tokens", 0) if usage else 0

    log_cost(
        feature=feature,
        model=selected_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
    )

    return answer


def ask_ai_with_tools(
    system_prompt,
    user_prompt,
    tools,
    tool_executor,
    model=None,
    temperature=0.1,
    feature="tool_calling",
    max_rounds=6,
):
    selected_model = model or PRIMARY_MODEL

    tool_definitions = [
        ChatCompletionsToolDefinition(
            function=FunctionDefinition(
                name=tool["name"],
                description=tool["description"],
                parameters=tool["parameters"],
            )
        )
        for tool in tools
    ]

    messages = [
        SystemMessage(content=system_prompt),
        UserMessage(content=user_prompt),
    ]

    for _ in range(max_rounds):
        response = client.complete(
            model=selected_model,
            messages=messages,
            tools=tool_definitions,
            temperature=temperature,
        )

        usage = getattr(response, "usage", None)
        input_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
        output_tokens = getattr(usage, "completion_tokens", 0) if usage else 0

        log_cost(
            feature=feature,
            model=selected_model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

        message = response.choices[0].message
        tool_calls = getattr(message, "tool_calls", None)

        if not tool_calls:
            return message.content or ""

        messages.append(
            AssistantMessage(
                content=message.content,
                tool_calls=tool_calls,
            )
        )

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            raw_args = tool_call.function.arguments or "{}"
            arguments = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
            result = tool_executor(function_name, arguments)
            payload = json.dumps(result) if not isinstance(result, str) else result

            messages.append(
                ToolMessage(
                    content=payload,
                    tool_call_id=tool_call.id,
                )
            )

    return "Tool calling exceeded maximum rounds. Review execution_trace.csv for details."
