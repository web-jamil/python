# Example of using escape characters in Python

# 1. Newline Escape Character (\n)
# The \n character creates a new line, splitting the string at this point.
print("Hello\nWorld")  # Output: Hello
# World

# 2. Tab Escape Character (\t)
# The \t character adds a tab space between words.
print("Hello\tWorld")  # Output: Hello    World

# 3. Backslash Escape Character (\\)
# The \\ character allows you to include a literal backslash in the string.
print("C:\\Users\\Name")  # Output: C:\Users\Name

# 4. Single Quote Escape Character (\' in single-quoted strings)
# The \' allows you to include a single quote inside a string wrapped in single quotes.
print('It\'s a great day')  # Output: It's a great day

# 5. Double Quote Escape Character (\" in double-quoted strings)
# The \" allows you to include a double quote inside a string wrapped in double quotes.
print("She said, \"Hello!\"")  # Output: She said, "Hello!"

# 6. Carriage Return Escape Character (\r)
# The \r moves the cursor to the beginning of the line, overwriting any text that follows.
print("Hello\rWorld")  # Output: Worldlo

# 7. Backspace Escape Character (\b)
# The \b removes the last character before it, effectively 'backspacing' the text.
print("Hello\bWorld")  # Output: HellWorld

# 8. Form Feed Escape Character (\f)
# The \f moves the cursor down one page (often doesn't show visible effect in most consoles).
print("Hello\fWorld")  # Output may vary depending on environment

# 9. Vertical Tab Escape Character (\v)
# The \v moves the cursor down vertically (usually not visible in most environments).
print("Hello\vWorld")  # Output may vary depending on environment

# 10. Unicode Escape Character (\u)
# The \u character represents a Unicode character using 4 hexadecimal digits.
print("\u0041")  # Output: A (Unicode for 'A')

# 11. Unicode Escape Character (\U for 8 hexadecimal digits)
# The \U character is used for characters with code points beyond U+FFFF.
print("\U0001F600")  # Output: 😀 (Unicode for Grinning Face emoji)

# 12. Unicode Escape by Name (\N{name})
# You can reference a Unicode character by its name using \N{name}.
print("\N{LATIN CAPITAL LETTER A}")  # Output: A
print("\N{GRINNING FACE}")  # Output: 😀 (Grinning Face emoji)

# 13. Raw String (r or R)
# A raw string treats backslashes as literal characters, making them useful for file paths and regular expressions.
print(r"Hello\nWorld")  # Output: Hello\nWorld (no escape processing)

# 14. File Path Example
# Using raw string to avoid escape sequences for file paths.
path = r"C:\Program Files\MyApp"
print(path)  # Output: C:\Program Files\MyApp

# 15. Multi-line String with Triple Quotes
# Triple quotes allow strings to span multiple lines without needing to explicitly use \n.
text = """This is a
multi-line string
in Python"""
print(text)
# Output:
# This is a
# multi-line string
# in Python
