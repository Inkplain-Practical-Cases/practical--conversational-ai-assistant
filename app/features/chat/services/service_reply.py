"""STEP-2 LLM service with injectable provider and deterministic offline fake.
ICS layer: service; CRD: be.service_reply
Called by handle_chat; calls llm_provider.complete.
Never put network credentials in the handler.
"""
from app.features.chat.providers.llm_provider import get_provider

def service_reply(message: str) -> str:
    """Use the injected LLM adapter, preserving the chat service contract."""
    return get_provider().complete(message)
