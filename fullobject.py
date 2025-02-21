# Inheritance
class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        pass
    
class CashPayment(Payment):
    def pay(self):
        print(f"Nqad pul bilan ${self.amount} tolandi.")
        
class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(f"Karta ({self.card_number[-4:]}) orqali ${self.amount} to‘landi.")

class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address  

    def pay(self):
        print(f"Kriptovalyuta hamyoniga ({self.wallet_address[:6]}...) ${self.amount} o‘tkazildi.")
        
cash = CashPayment(100)
card = CardPayment(250, "1234-5678-9876-5432")
crypto = CryptoPayment(500, "1A2b3C4d5E6f7G8H9I")

payments = [cash, card, crypto]

for payment in payments:
    payment.pay()
    

# absalute
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def pay(self):
        pass

class CashPayment(Payment):
    def pay(self):
        print(f"Naqd pul bilan ${self.amount} to‘landi.")
        
class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(f"Karta ({self.card_number[-4:]}) orqali ${self.amount} to‘landi.")

class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address  

    def pay(self):
        print(f"Kriptovalyuta hamyoniga ({self.wallet_address[:6]}...) ${self.amount} o‘tkazildi.")

cash = CashPayment(100)
card = CardPayment(250, "1234-5678-9876-5432")
crypto = CryptoPayment(500, "1A2b3C4d5E6f7G8H9I")

payments = [cash, card, crypto]

for payment in payments:
    payment.pay()


# Polymorphism
class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        raise NotImplementedError("pay metodi subclasslarda qayta yozilishi kerak.")

class CashPayment(Payment):
    def pay(self):
        return f"Naqd pul bilan ${self.amount} to‘landi."

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        return f"Karta ({self.card_number[-4:]}) orqali ${self.amount} to‘landi."

class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address  

    def pay(self):
        return f"Kriptovalyuta hamyoniga ({self.wallet_address[:6]}...) ${self.amount} o‘tkazildi."

payments = [
    CashPayment(100),
    CardPayment(250, "1234-5678-9876-5432"),
    CryptoPayment(500, "1A2b3C4d5E6f7G8H9I")
]

for payment in payments:
    print(payment.pay())


# Encapsulation
class Payment:
    def __init__(self, amount):
        self.__amount = amount  

    def get_amount(self):  
        """Xususiy qiymatni olish uchun getter metod"""
        return self.__amount

    def set_amount(self, new_amount):
        """Xususiy qiymatni o‘zgartirish uchun setter metod"""
        if new_amount > 0:
            self.__amount = new_amount
        else:
            raise ValueError("To‘lov summasi musbat bo‘lishi kerak.")

    def pay(self):
        raise NotImplementedError("pay metodi subclasslarda qayta yozilishi kerak.")

class CashPayment(Payment):
    def pay(self):
        return f"Naqd pul bilan ${self.get_amount()} to‘landi."

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.__card_number = card_number  

    def get_card_number(self):
        return self.__card_number[-4:]  

    def pay(self):
        return f"Karta ({self.get_card_number()}) orqali ${self.get_amount()} to‘landi."

class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.__wallet_address = wallet_address   

    def get_wallet_address(self):
        return self.__wallet_address[:6] + "..."

    def pay(self):
        return f"Kriptovalyuta hamyoniga ({self.get_wallet_address()}) ${self.get_amount()} o‘tkazildi."

class MobilePayment(Payment):
    def __init__(self, amount, phone_number):
        super().__init__(amount)
        self.__phone_number = phone_number 

    def get_phone_number(self):
        return self.__phone_number[-4:]  

    def pay(self):
        return f"Mobil to‘lov ({self.get_phone_number()}) orqali ${self.get_amount()} to‘landi."

payments = [
    CashPayment(100),
    CardPayment(250, "1234-5678-9876-5432"),
    CryptoPayment(500, "1A2b3C4d5E6f7G8H9I"),
    MobilePayment(150, "+998901234567")
]
def process_payments(payment_list):
    for payment in payment_list:
        print(payment.pay())

process_payments(payments)

card_payment = CardPayment(300, "9876-5432-1234-5678")
print("\nOldingi to‘lov summasi:", card_payment.get_amount())

card_payment.set_amount(350)
print("Yangi to‘lov summasi:", card_payment.get_amount())
