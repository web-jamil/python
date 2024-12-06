# logical_operators.py

# Logical AND (`and`) Operator
# The 'and' operator returns True if both conditions are True, otherwise False.

x = 10
y = 5

# Example 1: AND operator
# Checks if x is greater than 5 and y is less than 10
if x > 5 and y < 10:
    print("Both conditions are True.")  # Output: Both conditions are True.
else:
    print("At least one condition is False.")

# Logical OR (`or`) Operator
# The 'or' operator returns True if at least one of the conditions is True, otherwise False.

x = 3
y = 10

# Example 2: OR operator
# Checks if x is greater than 5 or y is less than 15
if x > 5 or y < 15:
    print("At least one condition is True.")  # Output: At least one condition is True.
else:
    print("Both conditions are False.")

# Logical NOT (`not`) Operator
# The 'not' operator negates the condition, returning True if the condition is False, and False if it is True.

x = 5

# Example 3: NOT operator
# Checks if x is not less than 10
if not x < 10:
    print("x is not less than 10.")  # Output: x is not less than 10.
else:
    print("x is less than 10.")

# Combining Logical Operators
# You can combine logical operators (and, or, not) to create more complex conditions.

x = 3
y = 10
z = 5

# Example 4: Combining AND, OR, and NOT operators
# Checks if x is greater than 2 and (y is less than 12 or z is not 5)
if x > 2 and (y < 12 or not z == 5):
    print("Condition is true.")  # Output: Condition is true.
else:
    print("Condition is false.")

# Using Logical Operators with Functions
# Logical operators can be used with functions that return boolean values.

def is_positive(x):
    """Returns True if x is positive, False otherwise."""
    return x > 0

def is_even(x):
    """Returns True if x is even, False otherwise."""
    return x % 2 == 0

x = 6

# Example 5: Logical operators with functions
# Checks if x is positive and even
if is_positive(x) and is_even(x):
    print("x is positive and even.")  # Output: x is positive and even.
else:
    print("x is either negative or odd.")

# Logical Operators with `if` Statements
# You can use logical operators directly in if-else statements to evaluate multiple conditions.

age = 18
has_license = True

# Example 6: AND operator with multiple conditions
# Checks if age is greater than 16 and has a driving license
if age > 16 and has_license:
    print("You are allowed to drive.")  # Output: You are allowed to drive.
else:
    print("You are not allowed to drive.")

x = 5
y = 3

# Example 7: OR operator with multiple conditions
# Checks if x is greater than 10 or y is less than 5
if x > 10 or y < 5:
    print("At least one condition is true.")  # Output: At least one condition is true.
else:
    print("Both conditions are false.")

x = 0

# Example 8: NOT operator in an if statement
# Checks if x is not equal to 10
if not x == 10:
    print("x is not 10.")  # Output: x is not 10.
else:
    print("x is 10.")

# Combining more complex conditions
# Example 9: Using all logical operators in a complex condition

a = 3
b = 7
c = 10

# Check if a is greater than 0, b is less than 10, and c is not equal to 5
if a > 0 and b < 10 and not c == 5:
    print("All conditions are True.")  # Output: All conditions are True.
else:
    print("At least one condition is False.")
