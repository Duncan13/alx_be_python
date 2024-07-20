class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        amount = 67.0
        self.account_balance = self.account_balance+amount
        print(f'Deposited: ${amount}')

    def withdraw(self,amount):
        amount = 50.0
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            print(f'Withdrew: ${amount}')
        else:
            print('Insufficient funds.')

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')

