class Payment:
    def process_payment(self, amount):
        print(f"მუშავდება გადახდა... თანხა: {amount} ლარი")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal-ით გადახდილია: {amount} ლარი")


def make_payment(payment_object, amount):
    payment_object.process_payment(amount)
    
payment = Payment()
cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

payment.process_payment(150)
make_payment(cc_payment, 150)  

print("="*40)

payment.process_payment(20)
make_payment(paypal_payment, 20)  