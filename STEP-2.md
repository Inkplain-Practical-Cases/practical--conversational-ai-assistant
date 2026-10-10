# STEP 2 of 6 — chat domain integration

This branch inherits STEP-1 and adds a provider boundary with deterministic offline behavior. Inspect app/features/chat/providers, then follow the handler to the service. Changes are intentionally small enough to test independently.

Run `python -m pytest -q` and `uvicorn app.main:app`. All STEP-1 contracts remain available. STEP-3 adds persistent state and/or richer orchestration.
