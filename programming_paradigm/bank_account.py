'''
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
'''

class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self,amount):
        #amount = int(input('Amount to be deposited: '))
        self.account_balance = self.account_balance+amount
       # print(f'Deposited: ${amount}')

    def withdraw(self,amount):
        amount = 0 # int(input('Amount to withdraw: '))
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            return amount
       # else:
            #print('Insufficient funds')

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')

