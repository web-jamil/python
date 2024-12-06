# Basic usage of enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    # index: Current position in the list
    # fruit: Current item in the list
    print(f"Index {index}: {fruit}")

# Starting the index from a custom value (e.g., 1)
for index, fruit in enumerate(fruits, start=1):
    # The 'start' parameter changes the starting index to 1
    print(f"Index {index}: {fruit}")

# Using enumerate with a list comprehension
# Creating a list of tuples with (index, fruit)
indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(indexed_fruits)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# Using enumerate with a tuple
colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    # Enumerate works with any iterable, including tuples
    print(f"Index {index}: {color}")

# Using enumerate with a string
name = "Python"
for index, char in enumerate(name):
    # Enumerate iterates through characters of the string with their indices
    print(f"Index {index}: {char}")

# Using enumerate with a dictionary (keys only)
person = {"name": "Alice", "age": 25, "city": "New York"}
for index, key in enumerate(person):
    # Enumerates the dictionary keys
    print(f"Index {index}: {key}")

# Using enumerate with a dictionary (keys and values)
for index, (key, value) in enumerate(person.items()):
    # Enumerates the key-value pairs in the dictionary
    print(f"Index {index}: {key} -> {value}")

# Enumerate with a custom generator function
def my_generator():
    yield "first"
    yield "second"
    yield "third"

for index, item in enumerate(my_generator(), start=100):
    # Enumerate works with custom generators and iterators
    print(f"Index {index}: {item}")

# Using enumerate with nested loops
matrix = [[1, 2], [3, 4], [5, 6]]
for row_index, row in enumerate(matrix):
    # Enumerates each row in the matrix
    print(f"Row {row_index}: {row}")
    for col_index, value in enumerate(row):
        # Enumerates each element in the row
        print(f"  Column {col_index}: {value}")

# Combining enumerate with break
# Stopping loop when a specific item is found
for index, fruit in enumerate(fruits):
    if fruit == "banana":
        print(f"Found banana at index {index}")
        break

# Combining enumerate with sorting
sorted_fruits = sorted(enumerate(fruits), key=lambda x: x[1])
# Enumerate combined with sorting returns (index, item) tuples
print(sorted_fruits)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
