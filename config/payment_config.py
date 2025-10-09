from enum import Enum

class PaymentType(Enum):
    """Enum for payment types"""
    PAYPAL = "paypal"
    GOOGLEPAY = "googlepay"
    CREDITCARD = "creditcard"
    BITCOIN = "bitcoin"

class PaymentConfig:
    """Configuration settings for payment processing"""
    
    MAX_AMOUNT = 10000.00
    MIN_AMOUNT = 0.01
    DEFAULT_CURRENCY = "USD"
    
    # Fee structures
    FEES = {
        PaymentType.PAYPAL.value: 0.029,
        PaymentType.GOOGLEPAY.value: 0.025,
        PaymentType.CREDITCARD.value: 0.035,
        PaymentType.BITCOIN.value: 0.001,
    }