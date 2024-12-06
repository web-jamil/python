def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome.__doc__) # Output: Checks if a string is a palindrome.
