class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        self.account_balance = self.account_balance+amount

    def withdraw(self,amount):
        if amount > self.account_balance:
            return amount > self.account_balance
        else:
            self.account_balance = self.account_balance-amount
            return self.account_balance
        

    def display_balance(self):
        return self.account_balance

