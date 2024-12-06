# Basic old-style formatting with strings
name = "Alice"
print("Hello, %s!" % name)  # Output: Hello, Alice! - %s is replaced by the value of name

# Using %d to format integers
age = 30
print("I am %d years old." % age)  # Output: I am 30 years old. - %d formats age as an integer

# Formatting floating point numbers with %f
pi = 3.14159265359
print("The value of pi is %f" % pi)  # Output: The value of pi is 3.141593 (default 6 decimal places)

# Formatting floating point numbers with specified precision (2 decimal places)
print("The value of pi is %.2f" % pi)  # Output: The value of pi is 3.14 - %.2f formats pi to 2 decimal places

# Using %x to format a number in hexadecimal (lowercase)
number = 255
print("Hexadecimal (lowercase): %x" % number)  # Output: Hexadecimal (lowercase): ff

# Using %X to format a number in hexadecimal (uppercase)
print("Hexadecimal (uppercase): %X" % number)  # Output: Hexadecimal (uppercase): FF

# Using %o to format a number in octal
print("Octal: %o" % number)  # Output: Octal: 377

# Formatting numbers in scientific notation with %e (lowercase e)
large_number = 1000000
print("Scientific notation (lowercase): %e" % large_number)  # Output: Scientific notation (lowercase): 1.000000e+06

# Formatting numbers in scientific notation with %E (uppercase E)
print("Scientific notation (uppercase): %E" % large_number)  # Output: Scientific notation (uppercase): 1.000000E+06

# Including a literal percentage symbol using %%
discount = 10
print("Discount: %d%%" % discount)  # Output: Discount: 10% - %% is used to print a literal %

# Formatting using a dictionary (using % and dictionary keys)
person = {"name": "Alice", "age": 25}
print("Name: %(name)s, Age: %(age)d" % person)  # Output: Name: Alice, Age: 25 - Using keys from the dictionary

# Using dynamic width (field width) with *
width = 10
print("%*s" % (width, "hello"))  # Output: "     hello" - Right-aligned with width of 10

# Left-aligning with dynamic width
print("%-*s" % (width, "hello"))  # Output: "hello     " - Left-aligned with width of 10

# Padding with zeros using %0nd
print("%010d" % 5)  # Output: 0000000005 - Pads the number with leading zeros to width of 10

# Using positional arguments (passing multiple values)
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Alice and I am 30 years old.

# Using multiple format specifiers in one string
first_name = "Alice"
last_name = "Johnson"
age = 30
print("Name: %s %s, Age: %d" % (first_name, last_name, age))  # Output: Name: Alice Johnson, Age: 30

# Formatting tuples (passing values as a tuple)
values = (255, 1000)
print("Hex: %x, Scientific: %e" % values)  # Output: Hex: ff, Scientific: 1.000000e+03

# Handling negative numbers with %d and %f
negative_number = -123
print("Negative integer: %d" % negative_number)  # Output: Negative integer: -123
print("Negative float: %.2f" % -45.678)  # Output: Negative float: -45.68

# Printing with multiple placeholders
print("The temperature is %d degrees and the humidity is %.2f%%." % (25, 72.5))  # Output: The temperature is 25 degrees and the humidity is 72.50%.

