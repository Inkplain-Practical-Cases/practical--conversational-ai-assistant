"""STEP-3 session persistence, isolated per tenant/session key."""
from collections import defaultdict
from threading import Lock
_lock=Lock()
_history=defaultdict(list)

def append_message(tenant_id:str,session_id:str,role:str,text:str)->list[dict[str,str]]:
    """Apply tenant isolation and bounded message retention."""
    if not tenant_id or not session_id:raise ValueError("Missing session owner")
    if role not in {"user","assistant"}:raise ValueError("Invalid role")
    with _lock:
        key=(tenant_id,session_id)
        _history[key].append({"role":role,"text":text})
        _history[key]=_history[key][-20:]
        return [dict(item) for item in _history[key]]

def read_messages(tenant_id:str,session_id:str)->list[dict[str,str]]:
    """Return detached history values so callers cannot mutate storage."""
    with _lock:
        return [dict(item) for item in _history.get((tenant_id,session_id),[])]
