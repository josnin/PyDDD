from app.message_bus import MessageBus
from app.unit_of_work import UnitOfWork
from domain.commands import CreateProductCommand

uow = UnitOfWork()
message_bus = MessageBus()
command = CreateProductCommand(name="SmartPhone", price=100.00, category="Electronics")

message_bus.handle(command, uow)

