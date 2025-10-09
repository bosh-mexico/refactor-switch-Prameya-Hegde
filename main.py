from services.payment_service import PaymentService
from factories.payment_factory import PaymentProcessorFactory
from processors.bitcoin_processor import BitcoinProcessor
from config.payment_config import PaymentType, PaymentConfig

def main():
    """Main function demonstrating modular payment processing"""
    amount = 150.75
    
    # Create different payment services
    services = {}
    for payment_type in ['paypal', 'googlepay', 'creditcard']:
        processor = PaymentProcessorFactory.create_processor(payment_type)
        services[payment_type] = PaymentService(processor)
    
    # Process payments with validation data
    services['paypal'].checkout(amount, email="user@example.com")
    services['googlepay'].checkout(amount, google_account="user@gmail.com")
    services['creditcard'].checkout(amount, card_number="1234567890123456", cvv="123")
    
    # Register and use Bitcoin processor (OCP in action)
    PaymentProcessorFactory.register_processor('bitcoin', BitcoinProcessor)
    bitcoin_processor = PaymentProcessorFactory.create_processor('bitcoin')
    bitcoin_service = PaymentService(bitcoin_processor)
    bitcoin_service.checkout(amount, wallet_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    
    # Display available processors
    print(f"Available processors: {PaymentProcessorFactory.get_available_processors()}")
    
    # Demonstrate processor switching (LSP)
    flexible_service = PaymentService(PaymentProcessorFactory.create_processor('paypal'))
    flexible_service.checkout(50.0, email="test@test.com")
    
    flexible_service.change_processor(PaymentProcessorFactory.create_processor('creditcard'))
    flexible_service.checkout(50.0, card_number="9876543210987654", cvv="456")

if __name__ == "__main__":
    main()