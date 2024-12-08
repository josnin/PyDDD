from abc import ABC

class DomainEvent(ABC):
    pass

class ProductCreated(DomainEvent):
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

