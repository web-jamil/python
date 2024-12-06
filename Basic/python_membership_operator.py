# Creating a Python code file with examples of membership operators and detailed comments

code_content = """
# Membership Operators in Python: Examples with Comments

# 1. Using 'in' to check membership in a list
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)  # True because 'apple' exists in the list
print('orange' in fruits)  # False because 'orange' is not in the list

# 2. Using 'not in' to check absence in a list
print('orange' not in fruits)  # True because 'orange' is not in the list
print('banana' not in fruits)  # False because 'banana' exists in the list

# 3. Using 'in' to check membership in a string
text = "Hello, world!"
print('Hello' in text)  # True because 'Hello' is a substring of the string
print('bye' in text)  # False because 'bye' is not in the string

# 4. Using 'not in' to check absence in a string
print('bye' not in text)  # True because 'bye' is not a substring
print('world' not in text)  # False because 'world' is a substring

# 5. Using 'in' with a dictionary (checks keys only)
person = {'name': 'Alice', 'age': 25}
print('name' in person)  # True because 'name' is a key in the dictionary
print('address' in person)  # False because 'address' is not a key

# 6. Using 'not in' with a dictionary (checks keys only)
print('address' not in person)  # True because 'address' is not a key
print('age' not in person)  # False because 'age' is a key

# 7. Using 'in' with a set
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # True because 3 is an element of the set
print(6 in numbers)  # False because 6 is not in the set

# 8. Using 'not in' with a set
print(6 not in numbers)  # True because 6 is not in the set
print(1 not in numbers)  # False because 1 is an element of the set
"""

# Define the file path to save the code
file_path = "/mnt/data/membership_operators_examples.py"

# Write the code to the file
with open(file_path, "w") as file:
    file.write(code_content)

file_path
