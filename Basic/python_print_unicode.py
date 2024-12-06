# 1. Printing Unicode Characters using Unicode Escape Sequences
print("\u0041")  # Prints the character 'A' using Unicode escape (U+0041)
print("\U0001F600")  # Prints the grinning face emoji (U+1F600)

# 2. Printing Unicode Characters Using the `chr()` Function
print(chr(65))  # Prints 'A', as the Unicode code point for 'A' is 65
print(chr(128512))  # Prints the grinning face emoji (Unicode code point U+1F600)

# 3. Printing Unicode Characters Using Unicode Names
import unicodedata
print(unicodedata.lookup('LATIN CAPITAL LETTER A'))  # Prints 'A'
print(unicodedata.lookup('GRINNING FACE'))  # Prints the grinning face emoji (U+1F600)

# 4. Printing Unicode Characters Directly in Strings
print("Python is fun 😊")  # Prints the string with an emoji directly included

# 5. Using Unicode in Regular Expressions
import re
match = re.match(r'\u0041', 'A')  # Matches the character 'A' using its Unicode escape
if match:
    print("Matched!")  # Prints "Matched!" if the character 'A' is found

# 6. Printing Unicode Characters Using `str.encode()`
string = "Hello"
encoded_string = string.encode('utf-8')  # Encodes string to bytes using UTF-8
print(encoded_string)  # Prints the byte representation of the string
decoded_string = encoded_string.decode('utf-8')  # Decodes back to a string
print(decoded_string)  # Prints 'Hello'

# 7. Unicode Characters in Formatted Strings (f-strings)
name = "Alice"
emoji = "😊"
print(f"Hello, {name} {emoji}")  # Prints "Hello, Alice 😊" using f-string with Unicode

# 8. Printing Unicode Characters Using `repr()`
print(repr("A"))  # Prints 'A' with repr() function (outputs string representation)
print(repr("😊"))  # Prints the Unicode escape sequence '\U0001F60A' for the emoji

# 9. Working with Unicode in Files (with Encoding)
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, 😊")  # Writes a string with an emoji to a file with UTF-8 encoding

with open('example.txt', 'r', encoding='utf-8') as f:
    print(f.read())  # Reads and prints the content of the file, including the emoji

# 10. Using Unicode Characters with `json` Module
import json
data = {"greeting": "Hello, 😊"}
json_data = json.dumps(data, ensure_ascii=False)  # Ensures Unicode characters are not escaped
print(json_data)  # Prints the JSON string with Unicode characters
