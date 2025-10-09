from typing import Dict, Type
from ..interfaces.payment_processor import PaymentProcessor
from ..processors.paypal_processor import PayPalProcessor
from ..processors.googlepay_processor import GooglePayProcessor
from ..processors.creditcard_processor import CreditCardProcessor

class PaymentProcessorFactory:
    """Factory for creating payment processors - follows OCP principle"""
    
    _processors: Dict[str, Type[PaymentProcessor]] = {
        'paypal': PayPalProcessor,
        'googlepay': GooglePayProcessor,
        'creditcard': CreditCardProcessor
    }
    
    @classmethod
    def create_processor(cls, payment_type: str) -> PaymentProcessor:
        """Create a payment processor instance"""
        processor_class = cls._processors.get(payment_type.lower())
        if processor_class:
            return processor_class()
        raise ValueError(f"Unsupported payment type: {payment_type}")
    
    @classmethod
    def register_processor(cls, payment_type: str, processor_class: Type[PaymentProcessor]):
        """Register a new processor without modifying existing code - OCP"""
        if not issubclass(processor_class, PaymentProcessor):
            raise TypeError("Processor must inherit from PaymentProcessor")
        cls._processors[payment_type.lower()] = processor_class
    
    @classmethod
    def get_available_processors(cls) -> list:
        """Get list of available payment processors"""
        return list(cls._processors.keys())