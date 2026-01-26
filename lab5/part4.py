name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

a, b, c = map(int, input("Enter three numbers: ").split())

print(f"Your numbers are {a}, {b}, {c}")
print("Sum:", a + b + c)
print("Average:", (a + b + c) / 3)
print("Product: ", a * b * c)