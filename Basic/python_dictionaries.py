# ================================
# Python Dictionaries: All About Syntaxes
# ================================

# ========== 1. Dictionary Basics ==========
# Creating dictionaries
empty_dict = {}                 # Empty dictionary
person = {"name": "John", "age": 30, "city": "New York"}
nested_dict = {"outer_key": {"inner_key": 42}}

print("Empty Dictionary:", empty_dict)
print("Person Dictionary:", person)
print("Nested Dictionary:", nested_dict)

# Using `dict()` constructor
constructed_dict = dict(name="Alice", age=25)
print("Constructed Dictionary:", constructed_dict)

# ========== 2. Accessing Elements ==========
# Access by key
print("Name:", person["name"])  # Output: John

# Using `.get()` (prevents KeyError)
print("Age:", person.get("age"))  # Output: 30
print("Unknown Key:", person.get("gender", "Not Found"))  # Output: Not Found

# Accessing nested elements
print("Inner Value:", nested_dict["outer_key"]["inner_key"])  # Output: 42

# ========== 3. Adding and Updating Elements ==========
# Add a new key-value pair
person["gender"] = "Male"
print("After Adding Gender:", person)

# Update an existing key
person["age"] = 31
print("After Updating Age:", person)

# Use `update()` to merge or add multiple key-value pairs
person.update({"city": "San Francisco", "hobby": "Cycling"})
print("After Update:", person)

# ========== 4. Removing Elements ==========
# Using `pop()` (removes and returns the value)
removed_value = person.pop("hobby")
print("Removed Hobby:", removed_value)
print("After pop:", person)

# Using `popitem()` (removes the last inserted key-value pair)
last_item = person.popitem()
print("Removed Last Item:", last_item)
print("After popitem:", person)

# Using `del` to remove a specific key
del person["city"]
print("After del:", person)

# Clear all key-value pairs
person.clear()
print("After clear:", person)

# ========== 5. Dictionary Operations ==========
# Keys, Values, and Items
person = {"name": "Alice", "age": 25}
print("Keys:", person.keys())          # Output: dict_keys(['name', 'age'])
print("Values:", person.values())      # Output: dict_values(['Alice', 25])
print("Items:", person.items())        # Output: dict_items([('name', 'Alice'), ('age', 25)])

# Checking if a key exists
print("Is 'name' in person?", "name" in person)  # Output: True
print("Is 'gender' not in person?", "gender" not in person)  # Output: True

# Dictionary Length
print("Dictionary Length:", len(person))  # Output: 2

# ========== 6. Iterating Over Dictionaries ==========
# Iterate over keys
for key in person:
    print("Key:", key)

# Iterate over values
for value in person.values():
    print("Value:", value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# ========== 7. Copying Dictionaries ==========
# Shallow copy
person_copy = person.copy()
print("Shallow Copy:", person_copy)

# Deep copy (for nested dictionaries)
import copy
nested = {"outer": {"inner": 1}}
nested_copy = copy.deepcopy(nested)
print("Deep Copy:", nested_copy)

# ========== 8. Dictionary Comprehensions ==========
# Create a dictionary with squares of numbers
squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Filtering in comprehensions
filtered_dict = {k: v for k, v in squares.items() if v > 10}
print("Filtered Dictionary:", filtered_dict)

# ========== 9. Merging Dictionaries ==========
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using `update()`
merged = dict1.copy()
merged.update(dict2)
print("Merged (update):", merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using `|` (Python 3.9+)
merged_new = dict1 | dict2
print("Merged (|):", merged_new)  # Output: {'a': 1, 'b': 3, 'c': 4}

# ========== 10. Advanced Dictionary Methods ==========
# Using `setdefault()`
person = {"name": "Alice", "age": 25}
default_value = person.setdefault("hobby", "Reading")
print("Set Default Hobby:", default_value)
print("After setdefault:", person)

# Using `fromkeys()` to create a dictionary
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print("Fromkeys Dictionary:", default_dict)

# Using `dict()` for key-value pairing
key_value_dict = dict(zip(["x", "y", "z"], [1, 2, 3]))
print("Key-Value Pairing:", key_value_dict)

# ========== 11. Nested Dictionaries ==========
# Creating and accessing nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}

print("Nested Dict:", nested_dict)
print("Person1 Name:", nested_dict["person1"]["name"])

# ========== 12. Common Use Cases ==========
# Counting occurrences of elements
from collections import Counter
data = ["apple", "banana", "apple", "cherry", "banana"]
counts = Counter(data)
print("Element Counts:", counts)  # Output: Counter({'apple': 2, 'banana': 2, 'cherry': 1})

# Default values with defaultdict
from collections import defaultdict
default_dict = defaultdict(int)
for item in data:
    default_dict[item] += 1
print("Default Dict Counts:", default_dict)

# Reverse key-value mapping
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print("Reversed Dictionary:", reversed_dict)

# ========== 13. Performance Considerations ==========
# Dictionary lookup time is O(1) (average case)
large_dict = {x: x**2 for x in range(1000000)}
print("Lookup example:", large_dict[999999])  # Output: 999998000001
