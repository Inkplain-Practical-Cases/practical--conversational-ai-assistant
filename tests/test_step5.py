from app.features.chat.services.retry_policy import with_bounded_retry
import pytest
def test_recovers_transient_error():
    count=[0]
    def run():
        count[0]+=1
        if count[0]==1:raise TimeoutError()
        return "ok"
    assert with_bounded_retry(run)== "ok"
    assert count[0]==2
def test_nontransient_not_retried():
    with pytest.raises(ValueError):with_bounded_retry(lambda:(_ for _ in ()).throw(ValueError("bad")))
