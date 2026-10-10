"""Regression tests for STEP-2+ fake model adapter and validation contracts."""
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_chat_round_trip(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER","fake")
    response=client.post("/api/chat",json={"session_id":"s-1","message":"Hello"})
    assert response.status_code==200
    assert response.json()=={"session_id":"s-1","answer":"Offline assistant: Hello"}

def test_rejects_empty_message():
    assert client.post("/api/chat",json={"session_id":"s-1","message":""}).status_code==422

def test_rejects_bad_session():
    assert client.post("/api/chat",json={"session_id":"../bad","message":"hi"}).status_code==422
