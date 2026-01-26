a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")

print(f"Input types: {type(a)}, {type(b)}, {type(c)}")

text = "12305"
num = int(text)
num_float = float(num)
print(type(num))
print(type(num_float))

persona = {
    "name": "Amaliia",
    "age": 21,
    "city": "Bishkek",
    "major": "Software Engineering"
}

print(f"{persona["name"]} is {persona['age']} and lives in {persona['city']}, styding {persona['major']}")

numbers = {1, 2, 3, 0, 4, 1, 5, 2, 9, 6}
print(numbers)

numbers.add(8)
print("After adding eight: ", numbers)

numbers.remove(0)
print("After removing zero: ", numbers)

print(4 in numbers)
# ten page in lab6