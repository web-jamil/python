# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

# Remove elemnt from set
s.remove(5)
print(s)


x = 10
y = 0

# Safe division using short-circuiting
print(y != 0 and (x / y > 1))  # False (short-circuits, no division by zero)

# Checking multiple conditions
print(x > 5 or y < 0)  # True (short-circuits after `x > 5`)


data = []
print(data and len(data) > 0)  # Evaluates to [] (short-circuits if data is empty)


value = None
result = value or "Default"
print(result)  # "Default" (short-circuits if `value` is None or False-like)
# If the first condition is True, the second condition is not evaluated.
print(True or print("This won't run"))  # Prints nothing

# Both conditions are evaluated only if the first is False.
print(False or print("This will run"))  # Prints: "This will run"
