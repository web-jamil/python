# Basic usage of f-string for embedding variables
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)
# Output: Hello, my name is Alice and I am 30 years old.

# Using expressions inside f-strings (mathematical operations)
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 10 and 5 is 15.

# Calling functions inside f-strings
def greet(name):
    return f"Hello, {name}"

print(f"{greet('Bob')}")
# Output: Hello, Bob

# Using f-strings with formatting (e.g., to 2 decimal places)
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")
# Output: Pi to 2 decimal places: 3.14

# Using f-strings for left, right, and center alignment
name = "Alice"
print(f"{name:<10} is left-aligned")
print(f"{name:>10} is right-aligned")
print(f"{name:^10} is center-aligned")
# Output:
# Alice      is left-aligned
#      Alice is right-aligned
#   Alice   is center-aligned

# Padding a number with leading zeros
number = 42
print(f"{number:05d}")
# Output: 00042

# Formatting large numbers with commas as thousand separators
large_number = 1000000
print(f"Large number: {large_number:,}")
# Output: Large number: 1,000,000

# Formatting DateTime objects in f-strings
from datetime import datetime
current_time = datetime.now()
print(f"Current date and time: {current_time:%Y-%m-%d %H:%M:%S}")
# Output: Current date and time: 2024-12-03 12:34:56

# Using conditional expressions inside f-strings
is_raining = True
print(f"It is {'raining' if is_raining else 'sunny'} today.")
# Output: It is raining today.

# Escaping curly braces in f-strings
print(f"{{Hello}}")  # Output: {Hello}
