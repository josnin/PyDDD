from abc import ABC

class Command(ABC):
    pass

class CreateProductCommand(Command):
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category