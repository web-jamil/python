# Example of a simple function
def greet(name):
    # Returns a greeting message with the provided name
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))  # Output: Hello, Alice!


# Example of a function with default parameters
def introduce(name, age=30):
    # Uses the default age if none is provided
    return f"{name} is {age} years old."

# Call the function with and without age
print(introduce("Bob"))          # Output: Bob is 30 years old.
print(introduce("Charlie", 25))  # Output: Charlie is 25 years old.


# Example of a function with positional arguments
def add(a, b):
    # Adds two numbers and returns the result
    return a + b

# Call the function
print(add(5, 10))  # Output: 15


# Example of a function with keyword arguments
def describe_pet(pet_name, animal_type="dog"):
    # Describes a pet using its name and type
    return f"{pet_name} is a {animal_type}."

# Call the function with positional and keyword arguments
print(describe_pet("Buddy"))                   # Output: Buddy is a dog.
print(describe_pet(pet_name="Mittens", animal_type="cat"))  # Output: Mittens is a cat.


# Example of a function with variable-length arguments
def print_numbers(*args):
    # Prints all the numbers passed as arguments
    for num in args:
        print(num)

# Call the function with multiple arguments
print_numbers(1, 2, 3, 4, 5)
# Output:
# 1
# 2
# 3
# 4
# 5


# Example of a function with variable-length keyword arguments
def person_details(**kwargs):
    # Prints the details of a person as key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments
person_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York


# Example of a recursive function
def factorial(n):
    # Calculates the factorial of a number recursively
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Call the function
print(factorial(5))  # Output: 120


# Example of a function with a return statement
def multiply(a, b):
    # Multiplies two numbers and returns the result
    return a * b

# Call the function
result = multiply(6, 7)
print(result)  # Output: 42


# Example of an anonymous function (lambda)
add = lambda x, y: x + y
# Call the lambda function
print(add(3, 4))  # Output: 7


# Example of a function with a docstring
def square(number):
    """
    Returns the square of a number.
    This is an example of a docstring.
    """
    return number ** 2

# Call the function and access the docstring
print(square(4))  # Output: 16
print(square.__doc__)
# Output:
# Returns the square of a number.
# This is an example of a docstring.


# Example of using global variables inside a function
x = 10  # Global variable

def modify_global():
    # Modifies the global variable
    global x
    x += 5

modify_global()
print(x)  # Output: 15


# Example of a generator function
def generate_numbers(n):
    # Yields numbers from 0 to n-1
    for i in range(n):
        yield i

# Use the generator
for num in generate_numbers(3):
    print(num)
# Output:
# 0
# 1
# 2


# Example of a decorator
def decorator(func):
    # A simple decorator that prints messages before and after a function call
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    # Prints a greeting message
    print("Hello!")

say_hello()
# Output:
# Before the function call
# Hello!
# After the function call
