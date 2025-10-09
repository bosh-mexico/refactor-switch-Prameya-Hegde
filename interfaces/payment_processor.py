from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processors following ISP & DIP principles"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment for the given amount"""
        pass
    
    @abstractmethod
    def validate_payment_data(self, **kwargs) -> bool:
        """Validate payment-specific data"""
        pass