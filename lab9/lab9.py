try:
    x = int(input("Enter a number: "))
    result = 15 / x
except ZeroDivisionError:
    print("Error: Can't divide by zero")
except ValueError:
    print("Error: Invalid input")
else:
    print(result)


try:
    file = open("It_All_Started_Fairly.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: file not found")
finally:
    print("Closing file")
    file.close()


def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Not enough money on balance")
    return balance - amount

try:
    new_balance = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")


class NegativeNumberError(Exception):
    def __init__(self, message = "Negative numbers are invalid"):
        self.message = message
        super().__init__(self.message)

def square__root(a):
    if a < 0:
        raise NegativeNumberError("Can't compute square root for negative numbers")
    return a ** 0.5

try:
    result = square__root(-16)
except NegativeNumberError as e:
    print(f"Error: {e}")
