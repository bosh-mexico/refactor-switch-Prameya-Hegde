from enum import Enum
from abc import ABC, abstractmethod

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        
        return True

class GooglePayProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing GooglePay payment of ${amount:.2f}")
        
        return True

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Credit Card payment of ${amount:.2f}")
        
        return True


class PaymentProcessorFactory:
    @staticmethod
    def create_processor(mode: PaymentMode) -> PaymentProcessor:
        processors = {
            PaymentMode.PAYPAL: PayPalProcessor(),
            PaymentMode.GOOGLEPAY: GooglePayProcessor(),
            PaymentMode.CREDITCARD: CreditCardProcessor()
        }
        
        processor = processors.get(mode)
        if processor is None:
            raise ValueError(f"Unsupported payment mode: {mode}")
        return processor


class CheckoutService:
    def __init__(self, processor_factory: PaymentProcessorFactory):
        self._processor_factory = processor_factory
    
    def checkout(self, mode: PaymentMode, amount: float) -> bool:
        try:
            processor = self._processor_factory.create_processor(mode)
            return processor.process_payment(amount)
        except ValueError as e:
            print(f"Checkout failed: {e}")
            return False


if __name__ == "__main__":
    amount = 150.75
    factory = PaymentProcessorFactory()
    checkout_service = CheckoutService(factory)

    checkout_service.checkout(PaymentMode.PAYPAL, amount)
    checkout_service.checkout(PaymentMode.GOOGLEPAY, amount)
    checkout_service.checkout(PaymentMode.CREDITCARD, amount)

    checkout_service.checkout(PaymentMode.UNKNOWN, amount)
