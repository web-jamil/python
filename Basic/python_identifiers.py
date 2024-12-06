# Valid Identifiers
age = 25  # Variable identifier
name = "John"  # Variable identifier
is_active = True  # Variable identifier (snake_case)
user_count = 100  # Variable identifier (snake_case)
_underscore_var = 10  # Valid identifier starting with an underscore

# Function Identifier
def calculate_sum(a, b):
    return a + b  # Function identifier, descriptive of its purpose

# Class Identifier (CamelCase)
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable identifier
        self.age = age  # Instance variable identifier

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Using the identifiers in code
person1 = Person("Alice", 30)  # Object identifier
person2 = Person("Bob", 25)

print(person1.greet())  # Using method identifier
print(person2.greet())  # Using method identifier

total = calculate_sum(5, 10)  # Using function identifier
print(total)  # Output will be 15

""" In Python, identifiers are names used to identify variables, functions, classes, modules, or other objects. An identifier is essentially any name you give to a Python object, and it follows certain naming rules and conventions.

Python Identifier Rules
Identifiers can include:

Letters (a-z, A-Z)
Digits (0-9), but not as the first character
Underscore (_)
Identifiers must start with:

A letter (a-z, A-Z) or an underscore (_).
Identifiers cannot start with:

A digit (0-9).
Identifiers are case-sensitive:

variable, Variable, and VARIABLE are considered different identifiers.
Reserved words (keywords):

You cannot use Python's reserved keywords (such as if, else, while, etc.) as identifiers.
Length:

There is no limit on the length of an identifier, but it is best practice to use meaningful and readable names.
Python Identifier Best Practices
Use descriptive names: Choose names that describe the role of the variable or function (e.g., age, total_cost).
Snake case for variables: Use underscores between words (e.g., total_amount, first_name).
Camel case for classes: Capitalize the first letter of each word (e.g., MyClass, CarModel).
Avoid single character names: Except for counters or iterators (e.g., i, j, k). """










""" False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
 """