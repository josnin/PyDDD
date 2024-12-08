from domain.models import Product
from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product):
        pass

    @abstractmethod
    def get(self, product_id: str) -> Product:
        pass
