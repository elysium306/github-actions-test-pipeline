from fastapi.testclient import TestClient
from app.main import app

def test_create_and_get_order():
    client = TestClient(app)

    create = client.post("/orders", json={"customer_id": "C123", "amount": 19.99})
    assert create.status_code == 201
    body = create.json()
    assert body["customer_id"] == "C123"
    assert body["amount"] == 19.99
    assert body["status"] == "CREATED"
    assert "id" in body

    order_id = body["id"]
    getr = client.get(f"/orders/{order_id}")
    assert getr.status_code == 200
    assert getr.json()["id"] == order_id

def test_get_missing_order_returns_404():
    client = TestClient(app)
    r = client.get("/orders/not-a-real-id")
    assert r.status_code == 404
