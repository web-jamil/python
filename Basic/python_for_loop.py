# Basic for loop iterating through a list
for i in [1, 2, 3]:
    print(i)  # prints each number in the list

# Using range() to loop a specific number of times
for i in range(5):  # Iterates from 0 to 4
    print(i)  # prints the number from 0 to 4

# Using range() with start, stop, and step
for i in range(1, 10, 2):  # Starts at 1, stops before 10, increments by 2
    print(i)  # prints 1, 3, 5, 7, 9

# Iterating over characters in a string
for char in "Python":
    print(char)  # prints each character in the string

# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # prints each fruit in the list

# Iterating through a dictionary (keys)
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key)  # prints keys from the dictionary

# Iterating through a dictionary (key-value pairs)
for key, value in person.items():
    print(key, value)  # prints both key and value from the dictionary

# Using enumerate() to iterate with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")  # prints index and fruit

# Nested for loop example
for i in range(2):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i = {i}, j = {j}")  # prints the values of i and j for each iteration

# List comprehension (compact for loop)
squares = [x**2 for x in range(5)]
print(squares)  # prints [0, 1, 4, 9, 16]

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # prints [0, 4, 16, 36, 64]

# Using zip() to iterate over two lists in parallel
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")  # prints name and age in parallel

# Using break to exit the loop
for i in range(5):
    if i == 3:
        break  # exits the loop when i equals 3
    print(i)  # prints 0, 1, 2

# Using continue to skip the current iteration
for i in range(5):
    if i == 3:
        continue  # skips the iteration when i equals 3
    print(i)  # prints 0, 1, 2, 4

# Using else with for loop
for i in range(3):
    print(i)  # prints 0, 1, 2
else:
    print("Loop completed without break.")  # prints after loop completes normally
