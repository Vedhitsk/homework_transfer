# 19.Create an abstract class Payment with an abstract method process_payment(). Implement CreditCardPayment and PayPalPayment subclasses.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing credit card payment of amount: {amount:.2f}")


class PayPalPayment(Payment):

    def process_payment(self, amount):
        print(f"Processing PayPal payment of amount: {amount:.2f}")


credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.process_payment(35000)
paypal.process_payment(20000)