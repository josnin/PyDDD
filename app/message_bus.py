from app import unit_of_work, handlers
from domain import commands, events

COMMAND_HANDLERS = {
    commands.CreateProductCommand: handlers.handle_create_product
}

EVENT_HANDLERS = {
    events.ProductCreated: [handlers.log_product_created, handlers.log_product_created2]
}

class MessageBus:
    def handle(self, message, uow: unit_of_work.UnitOfWork):
        """ dispatch message to appropriate handler(s) """
        if isinstance(message, commands.Command):
            handler = COMMAND_HANDLERS.get(type(message))
            if not handler:
                raise ValueError(f"No handler registered for command: {type(message)}")
            event = handler(message, uow)
            self._handle_event(event, uow)
        elif isinstance(message, events.DomainEvent):
            handlers = EVENT_HANDLERS.get(type(message), [])
            for handler in handlers:
                handler(message, uow)
        else:
            raise ValueError(f"Unknown message type {type(message)}")

    def _handle_event(self, event, uow):
        # handle the event locally by triggering event handlers
        handlers = EVENT_HANDLERS.get(type(event), [])
        for handler in handlers:
            handler(event, uow)

        # TODO?
        # publish the event  using the event publisher (Redis, Kafka, RabbitMQ, etc.?)






