from ..interfaces.payment_processor import PaymentProcessor

class PaymentService:
    """Payment service that handles checkout logic - follows SRP & DIP"""
    
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor
    
    def checkout(self, amount: float, **payment_data) -> bool:
        """Process checkout with validation"""
        if not self._validate_amount(amount):
            return False
        
        if not self.processor.validate_payment_data(**payment_data):
            print("Invalid payment data!")
            return False
            
        return self.processor.process_payment(amount)
    
    def _validate_amount(self, amount: float) -> bool:
        """Validate payment amount"""
        if amount <= 0:
            print("Invalid amount!")
            return False
        return True
    
    def change_processor(self, new_processor: PaymentProcessor):
        """Change payment processor at runtime - follows LSP"""
        self.processor = new_processor