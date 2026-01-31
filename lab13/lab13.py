import re

# Exercise 1
text = input("Please insert phone number, following 3x-4x pattern: ")
pattern = r"\d{3}-\d{4}"

numbers = re.findall(pattern, text)
print("Phone numbers:", numbers)

# Exercise 2
text = input("Please insert string starting with Hello: ")
pattern = r"Hello"

match = re.match(pattern, text)
search = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")

if search:
    print("Found in search:", search.group())
else:
    print("Not found in search")

# Exercise 3
text = input("Please insert text with numbers: ")
pattern = r"\d+"
replace = "NUMBER"

result = re.sub(pattern, replace, text)
print("Modified text:", result)

# Exercise 4
text = input("Please insert email addresses: ")
pattern = r"\b\w+@\w+\.\w+\b"

emails = re.findall(pattern, text)
print("Email addresses:", emails)

# Exercise 5
text = input("Please insert string: ")
pattern = r"\b[aeiouAEIOU]\w*\b"

words = re.findall(pattern, text, re.IGNORECASE)
print("Words starting with a vowel:", words)