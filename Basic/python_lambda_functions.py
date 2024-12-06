""" ### Comprehensive Guide to Lambda Functions in Python with Code and Comments

Lambda functions are anonymous functions in Python that can have any number of arguments but only one expression. They are defined using the `lambda` keyword and are typically used for short, concise operations.

### **Syntax of Lambda Functions**

```python
# General syntax
lambda arguments: expression
```

- **`arguments`**: Input parameters to the function, separated by commas.
- **`expression`**: A single expression evaluated and returned.

### **Examples with Code and Comments**

#### 1. **Basic Lambda Example**

```python
# A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

#### 2. **Lambda with No Arguments**

```python
# A lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!
```

#### 3. **Lambda with Single Argument**

```python
# A lambda function to square a number
square = lambda x: x * x
print(square(4))  # Output: 16
```

#### 4. **Lambda with Multiple Arguments**

```python
# A lambda function to find the maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Output: 20
```

#### 5. **Lambda Inside a Function**

```python
# A function that returns a lambda function to multiply numbers
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))  # Output: 10
```

#### 6. **Using Lambda with `map()`**

```python
# Using map() to square each number in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

#### 7. **Using Lambda with `filter()`**

```python
# Using filter() to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

#### 8. **Using Lambda with `reduce()`**

```python
from functools import reduce

# Using reduce() to calculate the product of all elements in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

#### 9. **Lambda with Conditional Expression**

```python
# A lambda function to check if a number is even or odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(5))  # Output: Odd
print(check_even(8))  # Output: Even
```

#### 10. **Lambda for Sorting**

```python
# Using lambda to sort a list of tuples by the second element
data = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(2, 'apple'), (1, 'banana'), (3, 'cherry')]
```

#### 11. **Lambda with List Comprehensions**

```python
# Using a lambda in a list comprehension
numbers = [1, 2, 3, 4]
squared = [(lambda x: x ** 2)(num) for num in numbers]
print(squared)  # Output: [1, 4, 9, 16]
```

#### 12. **Lambda with Default Arguments**

```python
# A lambda function with default values for arguments
add_default = lambda x, y=10: x + y
print(add_default(5))    # Output: 15
print(add_default(5, 20))  # Output: 25
```

#### 13. **Lambda for String Operations**

```python
# Using lambda to format a string
formatter = lambda name, age: f"My name is {name} and I am {age} years old."
print(formatter("Alice", 30))  # Output: My name is Alice and I am 30 years old.
```

#### 14. **Lambda with Nested Functions**

```python
# A lambda function inside another lambda function
nested_lambda = lambda x: lambda y: x + y
adder = nested_lambda(10)
print(adder(5))  # Output: 15
```

### **Best Practices**

1. **Use for Simple Operations**: Lambdas are best for short, simple functions.
2. **Avoid Complex Logic**: For more complicated operations, use `def` for better readability.
3. **Functional Programming**: Lambdas work well with `map()`, `filter()`, and `reduce()`.


### **Limitations of Lambda Functions**

1. **Single Expression**: Only one expression is allowed.
2. **Anonymous**: Lambdas have no name, making them harder to debug.
3. **Readability**: Overuse can reduce code readability.


### **Comparison with `def`**

| Feature                 | `lambda`                      | `def`               |
|-------------------------|-------------------------------|---------------------|
| **Definition**          | Single line, anonymous        | Multi-line, named   |
| **Use Case**            | Small, short-lived functions  | Complex logic       |
| **Readability**         | Less readable for complexity  | More readable       |


### **Example: Using Lambda vs `def`**

#### Using Lambda:
```python
# Lambda for doubling a number
double = lambda x: x * 2
print(double(4))  # Output: 8
```

#### Using `def`:
```python
# Named function for doubling a number
def double(x):
    return x * 2

print(double(4))  # Output: 8
```

This guide provides a thorough understanding of lambda functions in Python with real-world examples and comments. """


# Basic lambda function to square a number
square = lambda x: x * x  # A lambda with one argument to calculate square
print(square(4))  # Output: 16

# Lambda function with multiple arguments
add = lambda x, y: x + y  # Adds two numbers
print(add(3, 5))  # Output: 8

# Lambda with conditional logic
check_positive = lambda x: "Positive" if x > 0 else "Non-positive"  # Determines if a number is positive
print(check_positive(10))  # Output: Positive
print(check_positive(-5))  # Output: Non-positive

# Lambda used with map() to double numbers in a list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # Applies lambda to double each element
print(doubled)  # Output: [2, 4, 6, 8]

# Lambda used with filter() to find even numbers in a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filters even numbers from the list
print(even_numbers)  # Output: [2, 4]

# Lambda with reduce() to calculate the product of numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)  # Multiplies all elements together
print(product)  # Output: 24

# Lambda function inside another function
def multiplier(n):
    return lambda x: x * n  # Returns a lambda that multiplies by n

times_three = multiplier(3)  # Creates a function that multiplies by 3
print(times_three(5))  # Output: 15

# Lambda function for sorting a list of tuples by the second element
data = [(1, 'b'), (2, 'a'), (3, 'c')]
data.sort(key=lambda x: x[1])  # Sorts the list of tuples based on the second element
print(data)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# Lambda for reversing strings
reverse = lambda s: s[::-1]  # Reverses a string
print(reverse("lambda"))  # Output: adbmal

# Lambda for string formatting
formatter = lambda first, last: f"{first} {last}"  # Concatenates first and last names
print(formatter("John", "Doe"))  # Output: John Doe

# Lambda with list comprehensions
# Doubling numbers using lambda in list comprehension
doubled_list = [(lambda x: x * 2)(x) for x in numbers]
print(doubled_list)  # Output: [2, 4, 6, 8]

# Lambda for mixed data types in a list
data = [1, "apple", 3.5]
string_lengths = list(map(lambda x: len(str(x)), data))  # Finds the length of string representation of each item
print(string_lengths)  # Output: [1, 5, 3]
