from domain.commands import CreateProductCommand
from app import unit_of_work
from domain.events import ProductCreated
from uuid import uuid4

def handle_create_product(command: CreateProductCommand, uow: unit_of_work.UnitOfWork):
    # handle the command to create a product
    product_id = str(uuid4())
    print("Create product handler here")
    event = ProductCreated(product_id, command.name, command.price, command.category)

    return event

def log_product_created(event: ProductCreated, uow: unit_of_work.UnitOfWork):
    # handle the event by logging the product created
    print(f"Product Created: {event.product_id} - {event.name} ({event.price} {event.category})")

def log_product_created2(event: ProductCreated, uow: unit_of_work.UnitOfWork):
    # handle the event by logging the product created
    print(f"Product Created2: {event.product_id} - {event.name} ({event.price} {event.category})")
