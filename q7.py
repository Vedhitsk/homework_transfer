# 7.Modify the BankAccount class to include a getter method for checking the balance and a setter method to update it (ensuring balance cannot be set to a negative value).

class BankAccount:

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):

        if amount > 0: 
            self._balance += amount
            print("Amount ", amount, " has been credited successfully!")
            print("Total Balance: ", self._balance)
        
        else:
            print("Amount cannot be negative!")

    def withdraw(self, amount):
        if amount < 0:
            print("Amount cannot be negative!")

        elif self._balance - amount >= 0:
            self._balance -= amount
            print("Amount", amount, " has been debited successfully!")
            print("Total Balance: ", self._balance)
        
        else:
            print("Insufficient Balance")
            print("Total Balance: ", self._balance)

user1 = BankAccount()
user1.deposit(-50)
user1.withdraw(-50)