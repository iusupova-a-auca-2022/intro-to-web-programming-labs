import csv

# Exercise 1
name = "exercise1.txt"
text = """Basic Text File Operations Exercise 1.
It is a sample text!
Python program should create a text file with this exact text."""

with open(name, "w") as file:
    file.write(text)

with open(name, "r") as file:
    content = file.read()

print("Content from the file:")
print(content)
print()

# Exercise 2
dataset = [
    ["Patrick", "30", "Texas"],
    ["Mary", "25", "Madrid"],
    ["Penelope", "45", "Athens"],
    ["Mickey", "15", "New York"]
]

with open("exercise2.csv", "w", newline="") as file:
    data = csv.writer(file)
    data.writerows(dataset)

print("Content from the csv file:")

with open("exercise2.csv", "r", newline="") as file:
    content = csv.reader(file)

    for row in content:
        print(row)

print()

# Exercise 3
additional_text = "\nPython program should append this additional text to exercise1.txt."

with open(name, "a") as file:
    file.write(additional_text)

with open(name, "r") as file:
    content = file.read()

print("Content from the changed file:")
print(content)