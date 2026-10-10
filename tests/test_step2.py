from app.features.chat.services.service_reply import service_reply
from app.features.chat.providers.llm_provider import get_provider

def test_fake_provider_is_default(monkeypatch):
    monkeypatch.delenv("LLM_PROVIDER",raising=False)
    assert service_reply("hello")=="Offline assistant: hello"
def test_invalid_provider_fails_closed(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER","invalid")
    import pytest
    with pytest.raises(ValueError):get_provider()
