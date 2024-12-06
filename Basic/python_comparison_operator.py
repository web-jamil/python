# 1. Equal to (==)
x = 10
y = 10
print(x == y)  # True because x and y are equal

# 2. Not equal to (!=)
a = 5
b = 10
print(a != b)  # True because a is not equal to b

# 3. Greater than (>)
x = 15
y = 10
print(x > y)  # True because 15 is greater than 10

# 4. Less than (<)
x = 5
y = 10
print(x < y)  # True because 5 is less than 10

# 5. Greater than or equal to (>=)
x = 10
y = 5
print(x >= y)  # True because 10 is greater than 5

# 6. Less than or equal to (<=)
x = 5
y = 5
print(x <= y)  # True because 5 is equal to 5

# 7. Identity comparison (is)
x = [1, 2, 3]
y = x
print(x is y)  # True because x and y refer to the same object in memory

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False because a and b are different objects in memory

# 8. Identity not equal (is not)
x = [1, 2, 3]
y = x
print(x is not y)  # False because x and y are the same object

a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # True because a and b are different objects
