from collections import defaultdict
#import Command & DomainEvent 

class MessageBus:
    def __init__(self):
        self.command_handlers = {}
        self.event_handlers = defaultdict(list)

    def register_handler(self, message_type, handler):
        """ register a handler for commands """
        if isinstance(message_type, Command):
            self.command_handlers[message_type] = handler
        elif isinstance(message_type, DomainEvent):
            self.event_handlers[message_type].append(handler)
        else:
            raise ValueError(f"Unknown message type: {message_type}")

    def handle(self, message):
        """ dispatch message to appropriate handler(s) """
        if isinstance(message_type, Command):
            handler = self.command_handlers.get(type(message_type))
            if not handler:
                raise ValueError(f"No handler registered for command: {type(message_type}")

            # do we need this?
            return handler
        elif isinstance(message, DomainEvent):
            handlers = self.event_handlers.get(type(message_type), [])
            for handler in handlers:
                handler(message)
        else:
            raise ValueError(f"Unknown message type {type(message_type)}")




