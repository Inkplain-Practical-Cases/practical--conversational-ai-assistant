"""Combined chat use case with scoped history, fake model and bounded retry."""
from app.features.chat.providers.session_store import append_message, read_messages
from app.features.chat.services.retry_policy import with_bounded_retry
from app.features.chat.services.service_reply import service_reply

def chat_turn(tenant_id:str,session_id:str,message:str)->dict:
    """Execute one tenant-owned turn; no side-effecting external tool invoked."""
    if not tenant_id or not session_id or not message.strip():raise ValueError("Missing chat scope/input")
    append_message(tenant_id,session_id,"user",message.strip())
    answer=with_bounded_retry(lambda:service_reply(message))
    append_message(tenant_id,session_id,"assistant",answer)
    return {"session_id":session_id,"answer":answer,"history_count":len(read_messages(tenant_id,session_id))}
