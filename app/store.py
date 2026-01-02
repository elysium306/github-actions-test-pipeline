from typing import Dict
from app.models import Order, OrderCreate, new_order_id

class InMemoryStore:
    def __init__(self) -> None:
        self.orders: Dict[str, Order] = {}

    def create_order(self, payload: OrderCreate) -> Order:
        order = Order(id=new_order_id(), customer_id=payload.customer_id, amount=payload.amount)
        self.orders[order.id] = order
        return order

    def get_order(self, order_id: str) -> Order | None:
        return self.orders.get(order_id)
