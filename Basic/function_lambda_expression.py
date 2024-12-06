# Defining a simple function
def greet(name):
    # Returns a greeting message
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!

# Function with default arguments
def greet_with_default(name="Guest"):
    # Uses default value if no argument is provided
    return f"Hello, {name}!"
print(greet_with_default())  # Output: Hello, Guest!

# Function with variable-length arguments (*args)
def sum_numbers(*args):
    # Accepts multiple arguments and sums them
    return sum(args)
print(sum_numbers(1, 2, 3, 4))  # Output: 10

# Function with keyword arguments (**kwargs)
def print_user_info(**kwargs):
    # Iterates over keyword arguments and prints them
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_user_info(name="Alice", age=25, country="USA")

# Lambda function: square of a number
square = lambda x: x * x
print(square(4))  # Output: 16

# Lambda function with conditional logic
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(5))  # Output: Odd

# Using lambda with map() to double numbers in a list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]

# Using lambda with filter() to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted() for custom sorting
data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_data = sorted(data, key=lambda x: x[1])  # Sort by age
print(sorted_data)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

# Using lambda with reduce() to calculate the product
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24

# Higher-order function: accepts another function as an argument
def apply_function(func, value):
    # Applies the given function to the value
    return func(value)
print(apply_function(lambda x: x ** 2, 5))  # Output: 25

# Closure: a function returning a lambda
def multiplier(n):
    # Returns a lambda that multiplies input by n
    return lambda x: x * n
double = multiplier(2)
print(double(5))  # Output: 10

# Using lambda in a decorator
def uppercase_decorator(func):
    # Returns a new function that converts output to uppercase
    return lambda x: func(x).upper()
@uppercase_decorator
def say_hello(name):
    # Simple greeting function
    return f"Hello, {name}"
print(say_hello("Alice"))  # Output: HELLO, ALICE
