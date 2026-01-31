from abc import ABC, abstractmethod

class Student:
    university = "AUCA"

    def __init__(self, name, major, age):
        self.name = name
        self.major = major
        self.age = age

    def display_info(self):
        return f"{self.name} is a student of {self.major} and is {self.age} years old"

student = Student("April", "Software Engineering", 21)
print(student.display_info())

student.major = "TCMA"
print(student.display_info())

print(student.university)

del student.age
# print(student.age)

# Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.name} deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.name} withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("April", 15000)
account.deposit(1200)
account.withdraw(3000)

print(account.get_balance())

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Sound"

class Sheep(Animal):
    def make_sound(self):
        return "Bee!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

sheep = Sheep("Fluffy")
cow = Cow("MilkyWay")

print(sheep.name, "says:", sheep.make_sound())
print(cow.name, "says:", cow.make_sound())

# Polymorphism
class Human:
    def run(self):
        return "Runs at 45 km/h"

class Horse:
    def run(self):
        return "Runs faster than human at 87 km/h"

class Cheetah:
    def run(self):
        return "Runs faster than most animals at 110 km/h"

for obj in [Human(), Horse(), Cheetah()]:
    print(obj.run())

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car is running")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus is running")

car = Car()
bus = Bus()

car.start_engine()
bus.start_engine()

# Overriding
class Colors:
    def choose(self):
        print("You can choose a color from the palette")

class Red(Colors):
    def choose(self):
        print("You chose a red color!")

obj = Red()
obj.choose()