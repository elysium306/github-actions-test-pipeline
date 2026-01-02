from fastapi import FastAPI, HTTPException
from app.models import OrderCreate
from app.store import InMemoryStore

app = FastAPI(title="Quality Pipeline Demo API", version="1.0.0")
store = InMemoryStore()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/orders", status_code=201)
def create_order(payload: OrderCreate):
    return store.create_order(payload)

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = store.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
