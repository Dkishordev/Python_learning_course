class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no=acc

    def debit(self, amount):
        self.balance-= amount
        print(f"The amount ${amount} was debited.")
        print(f"Now the total balance is {self.get_balance()}")


    def credit(self, amount):
        self.balance+= amount
        print(f"The amount ${amount} was credited.")
        print(f"Now the total balance is {self.get_balance()}")
    
    def get_balance(self):
        return self.balance
    
acc1=Account(5000, '10012A')
acc1.debit(100)
acc1.credit(500)