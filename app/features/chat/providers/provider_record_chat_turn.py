"""Persist metadata-only chat session and turn records, never messages or replies."""
import hashlib
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

def provider_record_chat_turn(session_id: str, user_message: str, answer: str, db_path: str | None = None) -> None:
    """Record one reply event linked to a hashed session identity."""
    path = db_path or os.getenv("INKPLAIN_CHAT_DB", "data/chat_metadata.sqlite3")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    session_key = hashlib.sha256(session_id.encode("utf-8")).hexdigest()
    timestamp = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS chat_sessions (
            id TEXT PRIMARY KEY,
            created_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS chat_turns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL REFERENCES chat_sessions(id),
            user_char_count INTEGER NOT NULL,
            response_char_count INTEGER NOT NULL,
            occurred_at TEXT NOT NULL
        )""")
        connection.execute("INSERT OR IGNORE INTO chat_sessions(id, created_at) VALUES (?, ?)", (session_key, timestamp))
        connection.execute("INSERT INTO chat_turns(session_id, user_char_count, response_char_count, occurred_at) VALUES (?, ?, ?, ?)",
                           (session_key, len(user_message), len(answer), timestamp))
