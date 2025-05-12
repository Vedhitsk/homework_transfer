# 16.Overload the __str__ method in a class Bank to return a formatted string when the object is printed.

class Bank:

    def __init__(self, name, branch, balance):
        self.name = name
        self.branch = branch
        self.balance = balance

    def __str__(self):
        return f"Bank Name: {self.name}\nBranch: {self.branch}\nTotal Balance: Rs {self.balance:.2f}"


bank1 = Bank("State Bank of India", "Chennai", 500000)
print(bank1)
