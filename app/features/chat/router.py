"""HTTP door: delegate validated chat input to a handler.
ICS layer: door; CRD component: be.receive_chat
Called by: HTTP clients; Calls: handle_chat
Why it exists: isolates transport from chat behavior.
Without it: service rules would leak into routing.
Step: added in step 1.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.features.chat.handlers.handle_chat import handle_chat

router = APIRouter(prefix="/api", tags=["chat"])

class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1, max_length=80, pattern=r"^[a-zA-Z0-9_-]+$")
    message: str = Field(min_length=1, max_length=2000)

class ChatResponse(BaseModel):
    session_id: str
    answer: str

@router.post("/chat", response_model=ChatResponse)
def receive_chat(request: ChatRequest) -> ChatResponse:
    # Delegate to a typed handler; Pydantic rejects malformed requests with 422.
    return ChatResponse(**handle_chat(request.session_id, request.message))
