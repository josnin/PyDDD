from domain.models import Product

class UnitOfWork:
    def __init__(self):
        self.commited = False
        self.products = []
    
    def add(self, product: Product):
        self.products.append(product)

    def commit(self):
        self.commited = True
        print("Commiting change")

    def rollback(self):
        self.commited = False
        self.products.clear()
        print("Rolling back changes!")

