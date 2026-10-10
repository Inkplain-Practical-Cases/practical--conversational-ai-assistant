from app.features.chat.services.end_to_end import chat_turn
from app.features.chat.providers.session_store import read_messages

def test_scoped_turn(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER","fake")
    result=chat_turn("tenant-1","session-1","hello")
    assert result["history_count"]==2
    assert read_messages("tenant-2","session-1")==[]
