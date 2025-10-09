from ..interfaces.payment_processor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    """Credit Card payment processor - follows SRP"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Credit Card payment of ${amount:.2f}")
        # Credit Card-specific logic here
        return True
    
    def validate_payment_data(self, card_number: str = None, cvv: str = None, **kwargs) -> bool:
        """Validate credit card-specific data"""
        return (card_number is not None and len(card_number) >= 16 and
                cvv is not None and len(cvv) >= 3)