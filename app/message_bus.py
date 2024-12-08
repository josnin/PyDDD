from domain import commands, events
from unit_of_work import UnitOfWork
from domain.handlers import handle_create_product, log_product_created

COMMAND_HANDLERS = {
    commands.CreateProductCommand: handle_create_product
}

EVENT_HANDLERS = {
    events.ProductCreated: [log_product_created]
}

class MessageBus:
    #def __init__(self):
    #    self.command_handlers = {}
    #    self.event_handlers = defaultdict(list)

    def register_handler(self, message_type, handler):
        """ register a handler for commands """
        if issubclass(message_type, commands.Command):
            COMMAND_HANDLERS[message_type] = handler
        elif issubclass(message_type, events.DomainEvent):
            EVENT_HANDLERS[message_type].append(handler)
        else:
            raise ValueError(f"Unknown message type: {message_type}")

    def handle(self, message, uow: UnitOfWork):
        """ dispatch message to appropriate handler(s) """
        if isinstance(message, commands.Command):
            handler = self.command_handlers.get(type(message))
            if not handler:
                raise ValueError(f"No handler registered for command: {type(message)}")
            event = handler(message, uow)
            self._handle_event(event, uow)
        elif isinstance(message, events.DomainEvent):
            handlers = self.event_handlers.get(type(message), [])
            for handler in handlers:
                handler(message, uow)
        else:
            raise ValueError(f"Unknown message type {type(message)}")

    def _handle_event(self, event, uow):
        # handle the event locally by triggering event handlers
        handlers = self.event_handlers.get(type(event), [])
        for handler in handlers:
            handler(event, uow)

        # TODO?
        # publish the event  using the event publisher (Redis, Kafka, RabbitMQ, etc.?)






