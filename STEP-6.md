# STEP 6 of 6 — Integrate and harden chat

Install dependencies, run `python -m pytest -q`, and start `uvicorn app.main:app`. The full cumulative implementation provides tested local domain behavior and deterministic fixtures. The teaching code does **not** imply production approval, live services or all external adapters are complete. Audit the README limitations before deployment.

## Database (Entity) Relations
STEP-6 persists privacy-safe chat session and turn metadata in SQLite. `chat_sessions` uses a hashed session key; `chat_turns` links reply events using a foreign key. No user messages or model responses are stored. Configure `INKPLAIN_CHAT_DB` if needed. See STEP-6-ERD in the Simulator.
