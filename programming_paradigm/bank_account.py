class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self):
        amount = int(input('Amount to be deposited: '))
        self.account_balance = self.account_balance+amount
        print(f'Deposited: ${amount}')

    def withdraw(self):
        amount = int(input('Amount to withdraw: '))
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            print(f'Amount withdrawn: ${amount}')
        else:
            print('Insufficient funds')

    def display(self):
        print(f'Balance: ${self.account_balance}')

