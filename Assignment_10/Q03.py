class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)

account1 = BankAccount("Vedant", 1000)
account1.show_balance()
account1.deposit(500)
account1.show_balance()
account1.withdraw(300)
account1.show_balance()
account1.withdraw(1500)
