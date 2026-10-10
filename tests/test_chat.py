"""Regression tests for STEP-1 validated transport contracts."""
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_chat_round_trip():
    response = client.post("/api/chat", json={"session_id":"s-1","message":"Hello"})
    assert response.status_code == 200
    assert response.json() == {"session_id":"s-1","answer":"Received: Hello"}

def test_rejects_empty_message():
    assert client.post("/api/chat",json={"session_id":"s-1","message":""}).status_code == 422

def test_rejects_bad_session():
    assert client.post("/api/chat",json={"session_id":"../bad","message":"hi"}).status_code == 422
