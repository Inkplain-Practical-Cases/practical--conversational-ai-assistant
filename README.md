# Conversational AI Assistant

This is an Inkplain **Forward Deployed Engineering — Starter** teaching repository: a six-branch cumulative Python/FastAPI implementation.

## Learning path

| Step | Git branch | Capability |
|---|---|---|
| 1 | [`step-01-receive-validated-chat-requests`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-01-receive-validated-chat-requests) | Receive validated chat requests |
| 2 | [`step-02-add-openai-provider-adapter`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-02-add-openai-provider-adapter) | Add OpenAI provider adapter |
| 3 | [`step-03-persist-isolated-conversation-sessions`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-03-persist-isolated-conversation-sessions) | Persist isolated conversation sessions |
| 4 | [`step-04-execute-allowlisted-customer-tools`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-04-execute-allowlisted-customer-tools) | Execute allowlisted customer tools |
| 5 | [`step-05-handle-bounded-provider-failures`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-05-handle-bounded-provider-failures) | Handle bounded provider failures |
| 6 | [`step-06-harden-end-to-end-chat-service`](https://github.com/Inkplain-Practical-Cases/practical--conversational-ai-assistant/tree/step-06-harden-end-to-end-chat-service) | Harden end to end chat service |

## Run the final project

1. Use Python 3.12 or newer.
2. Copy `.env.example` to `.env` locally, without committing secrets.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m pytest -q`.
5. Run `uvicorn app.main:app --reload` and browse `/docs`.

Each STEP branch has a `STEP-N.crd` and `STEP-N.md`. Main contains `FINAL.crd`; a six-tab Simulator project file is generated in Stage 3 of the practical-case flow.

## Reliability and safety notes

This is an **educational reference implementation**, not a deployed production system. External providers and state stores use deterministic local fixtures where specified. Developers must not assume that the demo's in-memory tenancy, store, credential model, fake MCP transport or order reservations are production-hardened. Live service connections and durable transactional production integration require additional design and acceptance testing.

## Continuous integration

GitHub Actions workflow `.github/workflows/ci.yml` runs a seven-branch matrix covering all six cumulative STEP branches and main. The CI status must be checked; a committed workflow alone does not prove tests passed.

## Simulator and portal

The final CRD documents component relationships. The Stage 3 `conversational-ai-assistant.inkp` project will contain STEP-1 to STEP-6 tabs. Portal tutorials (Stage 4) link source examples to the specific branch so learners see exactly when each capability is introduced.
