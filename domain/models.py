from abc import ABC
from domain.value_objects import Money
from domain.enums import ProductCategory

class Entity(ABC):
    pass

class AggregateRoot(Entity):
    pass

class Product(AggregateRoot):
    def __init__(self, id, name, price: Money, category: ProductCategory):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def change_price(self, new_price: Money):
        self.price = new_price



