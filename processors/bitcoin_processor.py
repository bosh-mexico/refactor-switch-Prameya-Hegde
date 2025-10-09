from ..interfaces.payment_processor import PaymentProcessor

class BitcoinProcessor(PaymentProcessor):
    """Bitcoin payment processor - follows SRP"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Bitcoin payment of ${amount:.2f}")
        # Bitcoin-specific logic here
        return True
    
    def validate_payment_data(self, wallet_address: str = None, **kwargs) -> bool:
        """Validate Bitcoin-specific data"""
        return wallet_address is not None and len(wallet_address) >= 26