from ..interfaces.payment_processor import PaymentProcessor

class GooglePayProcessor(PaymentProcessor):
    """GooglePay payment processor - follows SRP"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # GooglePay-specific logic here
        return True
    
    def validate_payment_data(self, google_account: str = None, **kwargs) -> bool:
        """Validate GooglePay-specific data"""
        return google_account is not None