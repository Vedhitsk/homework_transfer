# 6.Create a class BankAccount with a private attribute _balance. Implement methods to deposit and withdraw money while ensuring the balance never goes negative.

class BankAccount:

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        print("Amount ", amount, " has been credited successfully!")
        print("Total Balance: ", self._balance)

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
            print("Amount", amount, " has been debited successfully!")
            print("Total Balance: ", self._balance)
        else:
            print("Insufficient Balance")
            print("Total Balance: ", self._balance)

user1 = BankAccount(100)
user1.deposit(50)
user1.withdraw(50)
