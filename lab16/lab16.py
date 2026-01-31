import json

# Exercise 1
student = {
    "name": "Alice",
    "age": 21,
    "major": "SFW",
    "year": "junior"
}

json_string = json.dumps(student, indent=4)

print("Student details in serialized JSON string:")
print(json_string)
print()

# Exercise 2
python_dictionary = json.loads(json_string)

print("Student details using deserialized Python object:")
print(python_dictionary)
print()

# Exercise 3
name = "exercise3.json"
dictionary = [
    {
        "name": "Mike",
        "age": 35,
        "occupation": "manager"
    },
    {
        "name": "Dory",
        "age": 49,
        "occupation": "director"
    }
]

with open(name, "w") as file:
    json.dump(dictionary, file, indent=4)

with open(name, "r") as file:
    content = json.load(file)

print("Content from JSON file:")
print(content)