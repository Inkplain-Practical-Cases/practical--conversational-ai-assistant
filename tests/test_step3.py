from app.features.chat.providers.session_store import append_message, read_messages
import pytest

def test_tenant_scoped_history():
    append_message("a","shared","user","private")
    assert read_messages("b","shared")==[]
def test_missing_owner_rejected():
    with pytest.raises(ValueError):append_message("","s","user","hello")
