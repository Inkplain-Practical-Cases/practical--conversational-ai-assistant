"""Chat handler; ICS layer handler, CRD be.handle_chat.
Called by: receive_chat; Calls: service_reply.
Why: preserve a boundary for future session ownership and authorization.
Without: door would need business orchestration.
Step: added in step 1.
"""
from app.features.chat.services.service_reply import service_reply

def handle_chat(session_id: str, message: str) -> dict[str, str]:
    """Pass validated fields to the reply service and shape the API result."""
    # The session ID is echoed but not persisted in the first learning slice.
    return {"session_id": session_id, "answer": service_reply(message)}
