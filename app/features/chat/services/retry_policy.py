"""Bounded retry for idempotent LLM read-style calls only."""
import time

def with_bounded_retry(operation,attempts:int=3,wait=lambda _:None):
    """Retry transient timeout/connection failures, then raise."""
    if attempts<1 or attempts>5:raise ValueError("Invalid retry budget")
    for index in range(attempts):
        try:return operation()
        except (TimeoutError,ConnectionError):
            if index==attempts-1:raise
            wait(index)
