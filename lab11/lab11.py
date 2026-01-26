# Exercise 1
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()

print(numbers)

for i in range(0, 3):
    print(numbers[i], end=" ")

print()
print(numbers[len(numbers) - 2], numbers[len(numbers) - 1])

i = len(numbers) - 1

while i >= 0:
    print(numbers[i], end=" ")
    i -= 1
print()


# Exercise 2
student = {"name": "ALice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student.update({"grade": "A+"})
student.pop("age")

print(student.keys())
print(student.values())
print(student.items())


# Exercise 3
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(union)
print(intersection)
print(difference)


# Exercise 4
colors = ("red", "blue", "green", "red", "yellow")
green_index = colors.index("green")
red_count = colors.count("red")

print(green_index)
print(red_count)


# Challenge Task
company = {"employees": [{"name": "Alice", "position": "Director", "salary": 25000},
                         {"name": "Richard", "position": "Manager", "salary": 20000},
                         {"name": "Peter", "position": "Developer", "salary": 19000}]}

company["employees"].append({"name": "Mira", "position": "Quality assurance", "salary": 18000})

for i in company["employees"]:
    print(i["name"])