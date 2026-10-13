"""Chat handler coordinates the reply and a privacy-safe persistent turn record.

The schema contains only a hashed session key and message lengths, never user text.
"""
from app.features.chat.services.service_reply import service_reply
from app.features.chat.providers.provider_record_chat_turn import provider_record_chat_turn

def handle_chat(session_id: str, message: str) -> dict[str, str]:
    """Return an unchanged API shape after recording a completed chat turn."""
    answer = service_reply(message)
    provider_record_chat_turn(session_id, message, answer)
    return {"session_id": session_id, "answer": answer}
