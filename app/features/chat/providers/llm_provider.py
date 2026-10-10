"""Provider abstraction: offline fake by default; optional OpenAI network adapter.
ICS layer: provider; CRD: be.llm_complete
Reason: isolates paid LLM I/O from domain logic and tests.
Step: added STEP-2.
"""
import os
from typing import Protocol

class LLMProvider(Protocol):
    def complete(self, message: str) -> str: ...

class FakeProvider:
    def complete(self, message: str) -> str:
        return "Offline assistant: " + message.strip()

class OpenAIProvider:
    def complete(self, message: str) -> str:
        # Import only for live mode; tests need no paid account.
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"],timeout=10)
        result=client.responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input=message)
        if not result.output_text:
            raise RuntimeError("Empty model output")
        return result.output_text

def get_provider() -> LLMProvider:
    """Fail closed for unknown configuration; offline by default."""
    mode=os.getenv("LLM_PROVIDER","fake")
    if mode=="fake":return FakeProvider()
    if mode=="openai":return OpenAIProvider()
    raise ValueError("Unsupported LLM_PROVIDER")
