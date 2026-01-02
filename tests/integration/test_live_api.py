import os
import pytest
import httpx

API_BASE_URL = os.getenv("API_BASE_URL", "").rstrip("/")

pytestmark = pytest.mark.integration

@pytest.mark.skipif(not API_BASE_URL, reason="API_BASE_URL not set")
def test_live_health_endpoint():
    r = httpx.get(f"{API_BASE_URL}/health", timeout=10)
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
