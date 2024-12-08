from domain.commands import CreateProductCommand
from unit_of_work import UnitOfWork
from domain.events import ProductCreated
from uuid import uuid4

def handle_create_product(command: CreateProductCommand, uow: UnitOfWork):
    # handle the command to create a product
    product_id = str(uuid4())
    event = ProductCreated(product_id, command.name, command.price, command.category)

    return event

def log_product_created(event: ProductCreated, uow: UnitOfWork):
    # handle the event by logging the product created
    print(f"Product Created: {event.product_id} - {event.name} ({event.price} {event.category})")
