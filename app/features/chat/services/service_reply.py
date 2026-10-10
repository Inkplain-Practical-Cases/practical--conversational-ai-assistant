"""Deterministic reply service; ICS layer service, CRD be.service_reply.
Called by: handle_chat; Calls: none.
Why: exercises the full HTTP-to-business path without external credentials.
Without: no testable chat output.
Step: added in step 1.
"""
def service_reply(message: str) -> str:
    """Return a deterministic acknowledgment, not a real model response."""
    # Do not claim an AI response until the provider adapter is introduced.
    return f"Received: {message.strip()}"
