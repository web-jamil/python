# Syntax: value_if_true if condition else value_if_false

# Example 1: Simple ternary operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Example 2: Nested ternary operator
num = 10
result = "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
print(result)  # Output: Positive

# Example 3: Assigning based on condition
x = 5
y = 10
max_value = x if x > y else y  # Assign the greater value of x and y
print(max_value)  # Output: 10

# Example 4: Ternary with function call
is_logged_in = False
message = "Welcome back!" if is_logged_in else "Please log in"
print(message)  # Output: Please log in
