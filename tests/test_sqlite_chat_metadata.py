"""Verify SQLite chat sessions/turns and absence of raw conversation text."""
import sqlite3
from app.features.chat.providers.provider_record_chat_turn import provider_record_chat_turn

def test_chat_session_turn_relation(tmp_path):
    path = str(tmp_path / "metadata.sqlite3")
    provider_record_chat_turn("session1", "Private message A", "Safe reply A", path)
    provider_record_chat_turn("session1", "Private message B", "Safe reply B", path)
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM chat_sessions").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM chat_turns").fetchone()[0] == 2
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
    with open(path,"rb") as file:
        content = file.read()
    assert b"Private message A" not in content
    assert b"Safe reply A" not in content
