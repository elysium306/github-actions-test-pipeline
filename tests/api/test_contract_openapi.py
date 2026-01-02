from app.main import app


def test_openapi_has_core_endpoints():
    schema = app.openapi()
    paths = schema.get("paths", {})
    assert "/health" in paths
    assert "/orders" in paths
    assert "/orders/{order_id}" in paths
