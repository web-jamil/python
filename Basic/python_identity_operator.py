# 1. Using 'is' to check if two variables refer to the same object in memory
x = 1000
y = 1000
print(x is y)  # False because they are stored separately (integers outside the cache range)

# Small integer caching (Python caches integers in a small range)
x = 256
y = 256
print(x is y)  # True because small integers are cached and refer to the same object

# 2. Using 'is' with mutable objects
a = [1, 2, 3]
b = a
print(a is b)  # True because both a and b refer to the same list object in memory

c = [1, 2, 3]
print(a is c)  # False because a and c are different objects in memory

# 3. Using 'is not' to check if two variables do not refer to the same object
x = [1, 2, 3]
y = x
print(x is not y)  # False because x and y refer to the same object in memory

a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # True because a and b are different objects, even though they have the same value

# 4. Checking for singleton objects like None
x = None
if x is None:
    print("x is None")  # This will print because x is None

# 5. Using 'is' with booleans (True, False are singletons)
x = True
y = True
print(x is y)  # True because True is a singleton object in Python

# 6. Using 'is not' to check for non-identity
x = None
y = 5
print(x is not y)  # True because x is None and y is an integer, different objects
