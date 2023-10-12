class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyX(self):
        amount = float(input("Enter the amount you want to add: "))
        self.balance += amount
        print(f"{amount} has been added to your account. Your new balance is {self.balance}")

    def kill(self):
        self.balance = 0
        print("Your account has been reset. Your new balance is 0")

    def __jackpot__(self):
        self.balance *= 10
        print(f"Your account has been multiplied by 10. Your new balance is {self.balance}")

    def __combine__(self, other):
        self.balance += other.balance
        print(f"The balance of {other.name} has been combined with your account. Your new balance is {self.balance}")




class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        if other.a == 0:
            raise ValueError("Division by zero is not allowed")
        return self.a / other.a
