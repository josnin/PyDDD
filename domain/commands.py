from abc import ABC
from dataclasses import dataclass
from domain import enums
import uuid


@dataclass
class CreateProductCommand:
    name: str
    price: float
    category: str

@dataclass
class ChangeStatusCommand:
    product_id: uuid.uuid4
    new_status: enums.ProductStatus


