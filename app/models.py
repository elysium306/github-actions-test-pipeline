from pydantic import BaseModel, Field
from typing import Literal
from uuid import uuid4

class OrderCreate(BaseModel):
    customer_id: str = Field(min_length=2)
    amount: float = Field(gt=0)

class Order(BaseModel):
    id: str
    customer_id: str
    amount: float
    status: Literal["CREATED", "PAID", "CANCELLED"] = "CREATED"

def new_order_id() -> str:
    return str(uuid4())
