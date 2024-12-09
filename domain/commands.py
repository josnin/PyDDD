from abc import ABC
from dataclasses import dataclass

class Command(ABC):
    pass

@dataclass
class CreateProductCommand(Command):
    name: str
    price: float
    category: str