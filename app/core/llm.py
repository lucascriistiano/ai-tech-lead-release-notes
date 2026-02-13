from __future__ import annotations

from app.core.config import get_settings


def chatgpt_text(system_prompt: str, user_prompt: str) -> str | None:
    """Generate a text response from ChatGPT if API credentials are configured."""
    settings = get_settings()
    if not settings.openai_api_key:
        return None

    try:
        from langchain_core.messages import HumanMessage, SystemMessage
        from langchain_openai import ChatOpenAI
    except Exception:
        return None

    llm = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=settings.openai_temperature,
    )

    try:
        response = llm.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt),
            ]
        )
    except Exception:
        return None

    if isinstance(response.content, str):
        return response.content.strip()

    return str(response.content).strip()
