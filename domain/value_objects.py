from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies!")
        
        return Money(self.amount + other.amount)