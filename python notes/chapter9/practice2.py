'''Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.'''

class Account:
    def __init__ (self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,Amount):
        self.balance-=Amount
        print("Rs.",Amount, "was debited")
        print("Total balance = ",self.get_balance())

    def credit(self,Amount):
        self.balance+=Amount
        print("Rs.",Amount, "was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

ac=Account(10000,789789)
ac.debit(999)
ac.credit(50)