class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance = self.account_balance+amount

    def withdraw(self,amount):
        amount = 50.0
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
        else:
            return False
        

    def display_balance(self):
        print('Current Balance: $',self.account_balance)

