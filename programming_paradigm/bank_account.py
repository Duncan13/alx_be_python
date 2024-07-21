class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        amount = 0
        if amount > self.account_balance:
            return "Insufficient funds"
        elif self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
        else:
            self.account_balance -= amount
            return self.account_balance

    def display_balance(self):
        return self.account_balance
