# Using the .format() method to insert values into a string

# Basic usage with positional arguments
greeting = "Hello, {}!".format("Alice")
print(greeting)  # Output: Hello, Alice!

# Using multiple positional arguments
name = "Bob"
age = 30
sentence = "{} is {} years old.".format(name, age)
print(sentence)  # Output: Bob is 30 years old.

# Using named placeholders with the .format() method
person = "Alice"
age = 25
sentence = "{name} is {age} years old.".format(name=person, age=age)
print(sentence)  # Output: Alice is 25 years old.

# Using positional and named arguments together
sentence = "{0} is {1} years old, and {0} likes programming.".format("Alice", 30)
print(sentence)  # Output: Alice is 30 years old, and Alice likes programming.

# You can also use dictionary unpacking
person_dict = {"name": "Charlie", "age": 35}
sentence = "{name} is {age} years old.".format(**person_dict)
print(sentence)  # Output: Charlie is 35 years old.

# Formatting numbers with .format()
pi = 3.14159265358979
formatted_pi = "Pi to 2 decimal places: {:.2f}".format(pi)
print(formatted_pi)  # Output: Pi to 2 decimal places: 3.14

# Formatting numbers with padding
number = 7
formatted_number = "The number is {:05d}".format(number)
print(formatted_number)  # Output: The number is 00007 - Pads with leading zeros to a width of 5

# Aligning text with .format()
text = "apple"
# Left-align within a field of 10 characters
left_aligned = "{:<10}".format(text)
print(left_aligned)  # Output: apple     (left-aligned in a 10-character wide field)

# Center-align within a field of 10 characters
center_aligned = "{:^10}".format(text)
print(center_aligned)  # Output:   apple   (center-aligned in a 10-character wide field)

# Right-align within a field of 10 characters
right_aligned = "{:>10}".format(text)
print(right_aligned)  # Output:      apple (right-aligned in a 10-character wide field)

# Formatting strings with dynamic width
width = 15
sentence = "This is a long sentence with a width of {0:{width}}".format("Text", width=width)
print(sentence)  # Output: This is a long sentence with a width of Text

# Using .format() with a mix of string and number
product = "laptop"
price = 1299.99
formatted_string = "The price of the {} is ${:.2f}".format(product, price)
print(formatted_string)  # Output: The price of the laptop is $1299.99

# Using .format() for nested values (with dictionaries)
product_info = {"product": "Laptop", "price": 1299.99}
sentence = "The price of the {product} is ${price:.2f}".format(**product_info)
print(sentence)  # Output: The price of the Laptop is $1299.99

# Using .format() to repeat items
sentence = "{0} {0} {0}".format("Hello")
print(sentence)  # Output: Hello Hello Hello

# Using .format() for padding strings with characters
sentence = "{:*^10}".format("Hello")
print(sentence)  # Output: **Hello*** (padded with asterisks to center the string)

# Using .format() with percentage formatting
percentage = 0.85
formatted_percentage = "The success rate is {:.2%}".format(percentage)
print(formatted_percentage)  # Output: The success rate is 85.00%

# Formatting large numbers with commas
large_number = 1234567
formatted_number = "{:,}".format(large_number)
print(formatted_number)  # Output: 1,234,567 (commas added as thousand separators)

# Using .format() for date formatting
from datetime import datetime
today = datetime.now()
formatted_date = "Today's date is {:%Y-%m-%d}".format(today)
print(formatted_date)  # Output: Today's date is 2024-12-03 (depending on the current date)

# Formatting floats and integers together
total = 245.6789
count = 10
sentence = "Total: {0:.2f}, Count: {1}".format(total, count)
print(sentence)  # Output: Total: 245.68, Count: 10

