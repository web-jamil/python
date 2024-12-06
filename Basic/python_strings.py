# ================================
# Python Strings: All About Syntaxes
# ================================

# ========== 1. String Basics ==========
# Creating strings
string1 = "Hello, World!"
string2 = 'Single quoted string'
multiline_string = """This is
a multiline
string."""
print("String 1:", string1)
print("String 2:", string2)
print("Multiline String:", multiline_string)

# String length
print("Length of String 1:", len(string1))

# ========== 2. String Indexing and Slicing ==========
# Accessing characters by index
print("First Character:", string1[0])
print("Last Character:", string1[-1])

# Slicing strings
print("Substring (0-5):", string1[:5])  # Output: Hello
print("Every Second Character:", string1[::2])  # Output: Hlo ol!

# Reversing a string
print("Reversed String:", string1[::-1])  # Output: !dlroW ,olleH

# ========== 3. String Immutability ==========
# Strings are immutable
try:
    string1[0] = "h"  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Create a new string
modified_string = "h" + string1[1:]
print("Modified String:", modified_string)

# ========== 4. String Concatenation and Repetition ==========
# Concatenation
greeting = "Hello" + ", " + "World!"
print("Concatenated String:", greeting)

# Repetition
repeated = "Repeat! " * 3
print("Repeated String:", repeated)

# ========== 5. Escape Characters ==========
# Using backslashes
escaped_string = "He said, \"This is an example.\""
print("Escaped String:", escaped_string)

# Special characters
newline_example = "Line1\nLine2"
tab_example = "Column1\tColumn2"
print("Newline Example:\n", newline_example)
print("Tab Example:\n", tab_example)

# Raw strings
raw_string = r"C:\Users\Example\Path"
print("Raw String:", raw_string)

# ========== 6. String Formatting ==========
# Old-style formatting
old_style = "Name: %s, Age: %d" % ("Alice", 25)
print("Old Style Formatting:", old_style)

# `str.format()`
formatted = "Name: {}, Age: {}".format("Bob", 30)
print("Formatted String:", formatted)

# f-strings (Python 3.6+)
name, age = "Charlie", 35
f_string = f"Name: {name}, Age: {age}"
print("f-string:", f_string)

# ========== 7. String Methods ==========
sample = "  Hello, Python World!  "

# Case-related methods
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Swapcase:", sample.swapcase())
print("Title Case:", sample.title())
print("Capitalize:", sample.capitalize())
print("Casefold (aggressive lower):", sample.casefold())

# Stripping and whitespace handling
print("Stripped String:", sample.strip())
print("Left Stripped:", sample.lstrip())
print("Right Stripped:", sample.rstrip())

# Search and replace
print("Starts with 'Hello':", sample.startswith("Hello"))
print("Ends with 'World!':", sample.endswith("World!"))
print("Find 'Python':", sample.find("Python"))
print("Replace 'World' with 'Universe':", sample.replace("World", "Universe"))

# Splitting and joining
words = sample.split()  # Split by whitespace
print("Split into Words:", words)
joined_string = " ".join(words)
print("Joined String:", joined_string)

# ========== 8. Querying Strings ==========
# Check properties
print("Is Alpha:", "Hello".isalpha())  # Only letters
print("Is Digit:", "12345".isdigit())  # Only digits
print("Is Alphanumeric:", "Hello123".isalnum())  # Letters + digits
print("Is Lowercase:", "hello".islower())
print("Is Uppercase:", "HELLO".isupper())
print("Contains Only Whitespace:", "   ".isspace())

# ========== 9. Advanced String Manipulation ==========
# Translating characters
trans_table = str.maketrans("aeiou", "12345")
translated = "hello".translate(trans_table)
print("Translated String:", translated)

# Partitioning
partitioned = sample.partition("Python")
print("Partitioned:", partitioned)  # Output: ('  Hello, ', 'Python', ' World!  ')

# ========== 10. String Encoding and Decoding ==========
# Encoding
encoded = "hello".encode("utf-8")
print("Encoded String:", encoded)  # Output: b'hello'

# Decoding
decoded = encoded.decode("utf-8")
print("Decoded String:", decoded)  # Output: hello

# ========== 11. String Comprehensions ==========
# Reverse each word in a sentence
sentence = "Python is amazing"
reversed_words = " ".join(word[::-1] for word in sentence.split())
print("Reversed Words:", reversed_words)

# Create a dictionary of word lengths
word_lengths = {word: len(word) for word in sentence.split()}
print("Word Lengths:", word_lengths)

# ========== 12. Common Use Cases ==========
# Remove vowels
vowels = "aeiouAEIOU"
no_vowels = "".join([ch for ch in sample if ch not in vowels])
print("String Without Vowels:", no_vowels)

# Count character occurrences
from collections import Counter
char_counts = Counter(sample)
print("Character Counts:", char_counts)

# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))  # Output: True
print("Is 'hello' a palindrome?", is_palindrome("hello"))  # Output: False

# ========== 13. Performance Considerations ==========
# String concatenation
# Inefficient way (creates new string each time)
result = ""
for i in range(5):
    result += str(i)
print("Concatenation Result:", result)

# Efficient way using `join()`
result = "".join(str(i) for i in range(5))
print("Efficient Concatenation Result:", result)

# Large string repetition
large_string = "A" * 10**6  # Efficiently creates a large string
print("Length of Large String:", len(large_string))

