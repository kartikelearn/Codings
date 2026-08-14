class Account:
    def __init__(self, acc, balance=0):
        self.acc = acc
        self.balance = balance

    def credit(self, amount):
        self.balance -= amount

    def debit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Your balance is:", self.balance)


s1 = Account("12345", 1000)   # account number and starting balance
s1.input()                    # interactively update
s1.show_balance()
