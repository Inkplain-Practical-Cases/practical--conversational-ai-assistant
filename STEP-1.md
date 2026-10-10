# STEP 1 of 6 — Receive validated chat requests

This is the first runnable slice of the conversational assistant: typed FastAPI ingress delegates through a handler to a deterministic service. There are no external model calls and session history is not stored yet.

## Run
`python -m pip install -r requirements.txt`
`python -m pytest -q`
`uvicorn app.main:app --reload`

## Verify
POST `/api/chat` with `{"session_id":"s-1","message":"Hello"}` returns a validated echo. Blank messages and invalid session keys return HTTP 422.

## Next
STEP-2: provider integration with a deterministic offline fake and explicit OpenAI adapter.
