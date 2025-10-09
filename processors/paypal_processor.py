from ..interfaces.payment_processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor - follows SRP"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        # PayPal-specific logic here
        return True
    
    def validate_payment_data(self, email: str = None, **kwargs) -> bool:
        """Validate PayPal-specific data"""
        return email is not None and "@" in email