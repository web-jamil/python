### Python `max()` Function: All About It

The `max()` function is a built-in Python function that returns the largest item in an iterable (like a list, tuple, or string) or the largest of two or more arguments. It is one of the most commonly used functions when you need to find the maximum value in a sequence of values or compare multiple values.

Here's a detailed breakdown of the `max()` function:

---

## **1. Syntax of `max()`**

```python
max(iterable, *, key=None, default=None)
max(arg1, arg2, *args, key=None)
```

- **iterable**: The iterable (list, tuple, string, etc.) whose largest item you want to return.
- **key**: Optional. A function to execute to decide the value to compare. The default value is `None`, which compares the elements directly.
- **default**: Optional. If the iterable is empty and no default is provided, a `ValueError` will be raised. If a default value is provided, it will be returned instead.

---

## **2. Basic Usage**

### **Find Maximum in an Iterable**

```python
numbers = [10, 20, 4, 45, 99]
result = max(numbers)
print(result)  # Output: 99
```

- In this example, `max()` finds the largest value in the list `numbers`.

---

### **Find Maximum from Multiple Arguments**

```python
result = max(10, 20, 4, 45, 99)
print(result)  # Output: 99
```

- Here, `max()` compares the numbers directly and returns the maximum value.

---

## **3. Using the `key` Argument**

The `key` argument is used when the elements in the iterable are more complex, such as tuples or objects, and you want to compare them based on a specific criterion (such as the length of strings or the value of a particular attribute).

### **Example with Strings (Find longest string)**

```python
words = ["apple", "banana", "cherry", "date"]
result = max(words, key=len)
print(result)  # Output: banana
```

- In this example, `max()` is used to find the longest word in the list based on the length of the strings.

### **Example with Tuples (Find based on second element)**

```python
points = [(1, 2), (3, 4), (5, 6)]
result = max(points, key=lambda x: x[1])
print(result)  # Output: (5, 6)
```

- Here, `max()` compares the second element of each tuple and returns the tuple with the highest second value.

---

## **4. Handling Empty Iterables with `default` Argument**

If the iterable is empty, and you don't provide the `default` argument, Python will raise a `ValueError`. However, if you provide a `default`, it will be returned instead of raising an error.

### **Example with Empty Iterable**

```python
numbers = []
result = max(numbers, default="No numbers")
print(result)  # Output: No numbers
```

- In this case, the list is empty, so the `default` value `"No numbers"` is returned instead of raising an exception.

---

## **5. Practical Use Cases of `max()`**

### **Finding the Largest Number in a List**

```python
numbers = [3, 9, 14, 27, 4]
max_number = max(numbers)
print(f"The largest number is: {max_number}")
```

### **Finding the Maximum in a Dictionary (based on values)**

You can also use `max()` to find the dictionary item with the highest value.

```python
grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92}
top_student = max(grades, key=grades.get)
print(f"The top student is: {top_student}")  # Output: Charlie
```

In this example, `grades.get` is used as the key to find the student with the highest grade.

---

## **6. Edge Cases to Consider**

- **Empty Iterable Without Default**:

  ```python
  numbers = []
  print(max(numbers))  # Raises ValueError: max() arg is an empty sequence
  ```

- **Multiple Maximum Values**:

  ```python
  numbers = [5, 9, 9, 5]
  print(max(numbers))  # Output: 9
  ```

  When there are multiple elements with the same maximum value, `max()` returns the first occurrence.

---

## **7. Performance Considerations**

- **Time Complexity**: The time complexity of `max()` is O(n), where n is the number of items in the iterable, because the function needs to check each element to determine the largest one.
- **Space Complexity**: The space complexity is O(1), since `max()` only needs a constant amount of space, regardless of the size of the iterable.

---

## **8. Summary**

The `max()` function is a powerful and flexible tool in Python for determining the largest element in a collection or comparing multiple values. Key features include:

- Finding the maximum from an iterable or multiple arguments.
- Using the `key` argument for complex comparisons.
- Providing a `default` to handle empty iterables.

By mastering the `max()` function, you can efficiently solve a wide range of problems involving comparisons in Python.

---

I hope this gives you a thorough understanding of how the `max()` function works in Python! Let me know if you need any more examples or clarifications.

Sure! Here's a more detailed and in-depth explanation of the `max()` function, including some additional examples, explanations of key features, and advanced use cases:

---

### **`max()` Function: Deep Dive**

The `max()` function is one of the most commonly used built-in functions in Python for determining the maximum value within a given iterable (e.g., list, tuple, etc.) or among multiple arguments. It can also be used in more complex scenarios involving custom comparison logic.

#### **Syntax Recap**

```python
max(iterable, *, key=None, default=None)
max(arg1, arg2, *args, key=None)
```

### **1. `max()` with Iterables**

The most common use of `max()` is to find the largest element in a sequence such as a list, tuple, or string.

#### **Basic Example:**

```python
numbers = [10, 5, 7, 25, 14]
result = max(numbers)
print(result)  # Output: 25
```

In this case, `max()` returns the largest value from the list `numbers`.

#### **String Example:**

```python
words = ['apple', 'banana', 'cherry', 'date']
result = max(words)
print(result)  # Output: 'date'
```

- The function compares the strings lexicographically, meaning it finds the one that comes last in alphabetical order.

### **2. `max()` with Multiple Arguments**

Instead of passing an iterable, you can pass multiple arguments to `max()` directly.

#### **Example with Multiple Values:**

```python
result = max(1, 2, 3, 5, 4)
print(result)  # Output: 5
```

In this example, `max()` compares the given numbers and returns the largest value, which is `5`.

### **3. Using the `key` Argument**

The `key` argument allows for custom comparison logic. You can provide a function or lambda that defines how the comparison is done.

#### **Example with Strings (Finding Longest String)**

```python
words = ['apple', 'banana', 'cherry', 'date']
longest_word = max(words, key=len)
print(longest_word)  # Output: 'banana'
```

- Here, `max()` uses the `len` function to find the word with the longest length.

#### **Example with Tuples (Find the Tuple with the Largest Second Element)**

```python
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
max_point = max(points, key=lambda x: x[1])
print(max_point)  # Output: (7, 8)
```

- In this case, we use a lambda function to compare the second element of each tuple and return the one with the largest second value.

### **4. Using the `default` Argument**

The `default` argument is useful when the iterable is empty. If the iterable is empty and `default` is not provided, Python raises a `ValueError`. By providing a `default`, we can prevent this error and return a default value.

#### **Example with Default:**

```python
empty_list = []
result = max(empty_list, default="No maximum found")
print(result)  # Output: No maximum found
```

- In this case, `max()` returns the string `"No maximum found"` instead of raising a `ValueError` since the list is empty.

### **5. Handling Multiple Maximum Values**

When multiple elements have the same maximum value, the `max()` function will return the first one it encounters.

#### **Example with Multiple Maximum Values:**

```python
numbers = [5, 9, 9, 5]
result = max(numbers)
print(result)  # Output: 9
```

- Here, the function returns the first `9`, even though there are multiple occurrences of `9` in the list.

### **6. Using `max()` with Dictionaries**

You can also use `max()` with dictionaries, for example, to find the dictionary key associated with the maximum value.

#### **Example with Dictionary:**

```python
grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 90}
top_student = max(grades, key=grades.get)
print(top_student)  # Output: 'Charlie'
```

- In this example, `grades.get` is used as the key function, which retrieves the value for each key in the dictionary, and `max()` returns the student with the highest grade.

### **7. `max()` with Iterators**

The `max()` function can also be used with iterators, such as those returned by `map()`, `filter()`, or other functions.

#### **Example with `map()` and `max()`:**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
max_squared = max(squared_numbers)
print(max_squared)  # Output: 25
```

- In this case, we use `map()` to square the numbers and then use `max()` to find the largest squared value.

---

## **Advanced Use Cases and Edge Cases**

### **8. Comparing Custom Objects**

If you're working with custom objects (like instances of a class), you can use the `key` argument to compare them based on specific attributes.

#### **Example with Custom Class:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
oldest = max(people, key=lambda p: p.age)
print(oldest.name)  # Output: Charlie
```

- In this example, we compare `Person` objects based on their `age` attribute to find the oldest person.

### **9. Handling Nested Iterables**

You can use `max()` on nested iterables (e.g., lists of lists) by defining a custom comparison key.

#### **Example with Nested Lists:**

```python
nested_list = [[1, 3], [5, 2], [9, 8], [2, 7]]
max_sublist = max(nested_list, key=lambda x: sum(x))
print(max_sublist)  # Output: [9, 8]
```

- Here, `max()` finds the sublist where the sum of its elements is the highest.

### **10. Performance Considerations**

- **Time Complexity**: The time complexity of `max()` is O(n), where n is the number of elements in the iterable. This is because `max()` must compare each element to find the largest one.
- **Space Complexity**: The space complexity is O(1) since `max()` only needs to store the current maximum value during the iteration.

---

## **Summary of `max()` Features:**

- Finds the largest item in an iterable or among multiple arguments.
- Can take an optional `key` function to customize the comparison.
- Handles empty iterables with the `default` argument, avoiding `ValueError`.
- Works with custom objects and nested iterables.
- Returns the first maximum if there are multiple maximum values.
- Performs a linear scan of the iterable, so the time complexity is O(n).

---

### **Common Errors with `max()`**

- **Empty Iterable**: Calling `max()` on an empty iterable without providing a `default` will raise a `ValueError`.

  ```python
  empty_list = []
  max(empty_list)  # Raises ValueError: max() arg is an empty sequence
  ```

- **Multiple Arguments**: `max()` can only take multiple arguments directly when they are provided as separate values, not as an iterable.

  ```python
  # Correct:
  max(1, 2, 3)

  # Incorrect:
  max([1, 2, 3])  # This is a single iterable, not multiple arguments
  ```

---

### **Conclusion**

The `max()` function is versatile and essential for working with sequences and collections in Python. By mastering it, you can handle a wide range of problems, from finding the largest number to complex object comparisons. Whether you are working with basic types or custom objects, `max()` provides a powerful way to find the maximum based on your specific needs.

Let me know if you need further explanations or more advanced examples!

The `max()` function in Python is a powerful and flexible tool that helps you find the largest element in an iterable or among multiple values. It can be customized using the `key` and `default` arguments, making it adaptable to many different use cases, from finding the largest number in a list to handling complex comparisons of custom objects.

### **Detailed Overview of the `max()` Function**

#### **1. Basic Usage with Iterables**

The most basic usage of `max()` is to find the largest element in an iterable like a list, tuple, or string.

- **Syntax:**

```python
max(iterable, *, key=None, default=None)
```

- `iterable`: This is the collection (list, tuple, etc.) from which you want to find the largest element.
- `key`: (optional) A function that takes a single argument and returns a value to use for comparison.
- `default`: (optional) A value that is returned if the iterable is empty.

#### **Example with a List of Numbers:**

```python
numbers = [10, 5, 8, 20, 14]
print(max(numbers))  # Output: 20
```

Here, `max()` simply finds the maximum value in the list, which is `20`.

#### **Example with a List of Strings (Lexicographical Comparison):**

```python
words = ["apple", "banana", "cherry", "date"]
print(max(words))  # Output: "date"
```

Since strings are compared lexicographically (alphabetical order), `max()` returns `"date"`, which comes last alphabetically.

---

#### **2. Finding the Maximum of Multiple Arguments**

You can pass multiple values directly to `max()` instead of an iterable.

- **Syntax:**

```python
max(arg1, arg2, *args, key=None)
```

- `arg1, arg2, *args`: These are the individual values you want to compare.

#### **Example with Multiple Numbers:**

```python
print(max(1, 2, 3, 5, 4))  # Output: 5
```

In this case, `max()` finds the maximum value among the arguments and returns `5`.

---

#### **3. Using the `key` Argument**

The `key` argument allows you to customize the comparison logic. It takes a function (such as a lambda or a predefined function) that extracts a value from each element in the iterable to compare.

##### **Example with Custom Key (Using `len()` to Find the Longest Word):**

```python
words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=len)
print(longest_word)  # Output: "banana"
```

Here, `max()` uses the `len` function as the key, so it compares the length of each word and returns the one with the longest length (`"banana"`).

##### **Example with Custom Key (Using a Lambda Function for Comparison):**

```python
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
max_point = max(points, key=lambda x: x[1])
print(max_point)  # Output: (7, 8)
```

Here, `max()` uses a lambda function to compare the second element of each tuple (i.e., `x[1]`) and returns the tuple `(7, 8)`.

---

#### **4. Handling Empty Iterables with `default` Argument**

If you pass an empty iterable to `max()` and do not specify the `default` argument, Python will raise a `ValueError`. To avoid this, you can use the `default` argument to specify a return value when the iterable is empty.

- **Syntax:**

```python
max(iterable, *, key=None, default=None)
```

#### **Example with Empty Iterable:**

```python
empty_list = []
print(max(empty_list, default="No items"))  # Output: No items
```

In this case, the empty list returns the default value `"No items"` instead of raising an error.

---

#### **5. Finding the Maximum from a Dictionary**

You can also use `max()` with dictionaries. By default, `max()` works with the keys of the dictionary, but you can specify a `key` argument to find the key corresponding to the maximum value.

##### **Example (Maximum Key Based on Values):**

```python
grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 90}
top_student = max(grades, key=grades.get)
print(top_student)  # Output: Charlie
```

Here, `max()` uses the `grades.get` function to compare the values and find the key (`'Charlie'`) with the highest value.

---

#### **6. Using `max()` with Iterators**

`max()` can also be used with iterators (such as those returned by functions like `map()` or `filter()`). These iterators generate elements lazily, meaning they do not require all elements to be stored in memory.

##### **Example with `map()` and `max()`:**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
max_squared = max(squared_numbers)
print(max_squared)  # Output: 25
```

Here, we use `map()` to square the numbers in the list, and then `max()` is used to find the largest squared number.

---

#### **7. Handling Multiple Maximum Values**

When multiple elements have the same maximum value, `max()` will return the first occurrence of that value.

##### **Example with Duplicate Maximum Values:**

```python
numbers = [5, 9, 9, 5]
result = max(numbers)
print(result)  # Output: 9
```

In this case, both `9` and `9` are the largest values, but `max()` returns the first occurrence (`9`).

---

#### **8. Performance Considerations**

- **Time Complexity**: The time complexity of `max()` is O(n), where n is the number of elements in the iterable. This is because `max()` has to compare each element once to find the maximum.
- **Space Complexity**: The space complexity is O(1), meaning that `max()` does not use extra memory for storing values, it only keeps track of the largest value found during iteration.

---

### **Advanced Use Cases of `max()`**

#### **9. Comparing Custom Objects**

If you're working with custom objects, you can use the `key` argument to specify how to compare them based on their attributes.

##### **Example with Custom Class:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
oldest = max(people, key=lambda p: p.age)
print(oldest.name)  # Output: Charlie
```

Here, `max()` compares instances of the `Person` class based on their `age` attribute and returns the `Person` object with the highest age.

#### **10. Handling Nested Iterables**

When working with nested lists or multi-dimensional arrays, you can use `max()` to find the element based on a custom condition, such as comparing sums, averages, or other metrics of the nested elements.

##### **Example with Nested Lists:**

```python
nested_list = [[1, 3], [5, 2], [9, 8], [2, 7]]
max_sublist = max(nested_list, key=lambda x: sum(x))
print(max_sublist)  # Output: [9, 8]
```

In this example, `max()` compares the sums of each sublist and returns the one with the largest sum (`[9, 8]`).

---

### **Common Pitfalls with `max()`**

1. **Empty Iterable**: Passing an empty iterable to `max()` without providing a `default` will raise a `ValueError`.

   ```python
   max([])  # Raises ValueError: max() arg is an empty sequence
   ```

2. **Incorrect Usage with Multiple Arguments**: You can pass multiple arguments to `max()`, but they need to be separate values, not a single iterable.

   ```python
   max([1, 2, 3])  # Incorrect, you should pass the values as separate arguments: max(1, 2, 3)
   ```

---

### **Conclusion**

The `max()` function is a powerful and versatile built-in function that allows for both simple and advanced comparisons. From finding the largest number in a list to comparing custom objects based on complex criteria, `max()` provides an elegant way to retrieve the largest item from various types of iterables or direct arguments.

By mastering the `key` and `default` arguments, you can tailor `max()` to fit a wide range of scenarios, making it an indispensable tool for Python programming.

Here are various examples of the `max()` function in Python, explained with detailed code and comments to demonstrate its usage and versatility:

---

### **1. Basic Usage: Finding Maximum in a List**

```python
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Find the maximum number in the list
max_number = max(numbers)

# Print the result
print("Maximum number:", max_number)
# Output: Maximum number: 50
```

---

### **2. Using `max()` with Strings**

```python
# List of words
words = ["apple", "banana", "cherry", "date"]

# Find the word that is lexicographically largest
largest_word = max(words)

# Print the result
print("Largest word:", largest_word)
# Output: Largest word: date
```

Here, `max()` compares words alphabetically, so `"date"` is considered the largest.

---

### **3. Using `max()` with Multiple Arguments**

```python
# Using multiple arguments directly
max_value = max(100, 200, 50, 300, 150)

# Print the result
print("Maximum value:", max_value)
# Output: Maximum value: 300
```

---

### **4. Using the `key` Argument**

#### **Example 1: Finding the Longest Word**

```python
# List of words
words = ["apple", "banana", "cherry", "date"]

# Find the longest word using the key argument
longest_word = max(words, key=len)

# Print the result
print("Longest word:", longest_word)
# Output: Longest word: banana
```

Here, `key=len` tells `max()` to compare the lengths of the words.

---

#### **Example 2: Finding the Tuple with the Largest Second Element**

```python
# List of tuples
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Find the tuple with the largest second element
max_point = max(points, key=lambda x: x[1])

# Print the result
print("Point with the largest second element:", max_point)
# Output: Point with the largest second element: (7, 8)
```

Here, a lambda function (`lambda x: x[1]`) is used to extract the second element of each tuple for comparison.

---

### **5. Handling Empty Iterables with the `default` Argument**

```python
# An empty list
empty_list = []

# Using max() with a default value
max_value = max(empty_list, default="No items")

# Print the result
print("Maximum value:", max_value)
# Output: Maximum value: No items
```

The `default` argument ensures that `max()` does not raise an error when the iterable is empty.

---

### **6. Finding the Maximum from a Dictionary**

#### **Example: Finding the Key with the Maximum Value**

```python
# Dictionary of student grades
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}

# Find the key (student name) with the highest grade
top_student = max(grades, key=grades.get)

# Print the result
print("Top student:", top_student)
# Output: Top student: Bob
```

Here, `grades.get` is used to extract values (grades) for comparison, while `max()` returns the corresponding key (student name).

---

### **7. Using `max()` with Custom Objects**

```python
# Define a custom class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# List of Person objects
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]

# Find the person with the maximum age
oldest_person = max(people, key=lambda p: p.age)

# Print the result
print("Oldest person:", oldest_person.name)
# Output: Oldest person: Charlie
```

Here, the lambda function extracts the `age` attribute for comparison.

---

### **8. Using `max()` with Nested Iterables**

```python
# Nested list of numbers
nested_list = [[1, 3], [5, 2], [9, 8], [2, 7]]

# Find the sublist with the largest sum
max_sublist = max(nested_list, key=sum)

# Print the result
print("Sublist with the largest sum:", max_sublist)
# Output: Sublist with the largest sum: [9, 8]
```

In this example, `sum` is used as the key to compare the total of each sublist.

---

### **9. Comparing Elements in Iterators**

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Square each number using map, then find the maximum squared value
max_squared = max(map(lambda x: x**2, numbers))

# Print the result
print("Maximum squared value:", max_squared)
# Output: Maximum squared value: 25
```

---

### **10. Comparing Items with Duplicate Maximum Values**

```python
# List with duplicate maximum values
numbers = [5, 9, 9, 5]

# Find the first occurrence of the maximum value
max_number = max(numbers)

# Print the result
print("Maximum number:", max_number)
# Output: Maximum number: 9
```

When there are duplicates, `max()` returns the first occurrence of the maximum value.

---

### **Conclusion**

The `max()` function is a versatile tool that can handle simple comparisons, custom comparisons using the `key` argument, and default values for empty iterables. Its flexibility makes it an essential function for both basic and advanced Python programming tasks.

Here is the `max()` function explained through code examples with comments only:

---

```python
# Example 1: Basic usage with a list of numbers
numbers = [10, 20, 30, 40, 50]
max_number = max(numbers)  # Find the maximum number in the list
print("Maximum number:", max_number)  # Output: 50
```

---

```python
# Example 2: Find the lexicographically largest string
words = ["apple", "banana", "cherry", "date"]
largest_word = max(words)  # Compare alphabetically
print("Largest word:", largest_word)  # Output: date
```

---

```python
# Example 3: Using multiple arguments
max_value = max(100, 200, 50, 300, 150)  # Pass values directly
print("Maximum value:", max_value)  # Output: 300
```

---

```python
# Example 4: Using the key argument to find the longest word
words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=len)  # Compare based on length
print("Longest word:", longest_word)  # Output: banana
```

---

```python
# Example 5: Finding a tuple with the largest second element
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
max_point = max(points, key=lambda x: x[1])  # Compare second elements
print("Point with the largest second element:", max_point)  # Output: (7, 8)
```

---

```python
# Example 6: Handling empty iterables with the default argument
empty_list = []
max_value = max(empty_list, default="No items")  # Provide a default value
print("Maximum value:", max_value)  # Output: No items
```

---

```python
# Example 7: Finding the key with the highest value in a dictionary
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
top_student = max(grades, key=grades.get)  # Compare values (grades)
print("Top student:", top_student)  # Output: Bob
```

---

```python
# Example 8: Comparing custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
oldest_person = max(people, key=lambda p: p.age)  # Compare ages
print("Oldest person:", oldest_person.name)  # Output: Charlie
```

---

```python
# Example 9: Finding the sublist with the largest sum
nested_list = [[1, 3], [5, 2], [9, 8], [2, 7]]
max_sublist = max(nested_list, key=sum)  # Compare by the sum of elements
print("Sublist with the largest sum:", max_sublist)  # Output: [9, 8]
```

---

```python
# Example 10: Find the maximum squared value
numbers = [1, 2, 3, 4, 5]
max_squared = max(map(lambda x: x**2, numbers))  # Square each number and find the max
print("Maximum squared value:", max_squared)  # Output: 25
```

---

```python
# Example 11: Handle duplicates in a list
numbers = [5, 9, 9, 5]
max_number = max(numbers)  # Returns the first occurrence of the maximum value
print("Maximum number:", max_number)  # Output: 9
```

```python
# Example 1: Finding the maximum number in a list
numbers = [1, 2, 3, 4, 5]
max_value = max(numbers)  # Finds the largest number in the list
print("Maximum value:", max_value)  # Output: 5
```

```python
# Example 2: Finding the maximum string lexicographically
strings = ["apple", "banana", "cherry"]
largest_string = max(strings)  # Compares strings alphabetically
print("Largest string:", largest_string)  # Output: cherry
```

```python
# Example 3: Using max with multiple arguments
max_result = max(10, 20, 5, 30)  # Finds the maximum from the given numbers
print("Maximum result:", max_result)  # Output: 30
```

```python
# Example 4: Using the key parameter to find the longest string
words = ["cat", "elephant", "dog"]
longest_word = max(words, key=len)  # Finds the string with the maximum length
print("Longest word:", longest_word)  # Output: elephant
```

```python
# Example 5: Finding the maximum tuple by its second element
tuples = [(1, 10), (2, 20), (3, 15)]
max_tuple = max(tuples, key=lambda x: x[1])  # Compares by the second element
print("Tuple with largest second value:", max_tuple)  # Output: (2, 20)
```

```python
# Example 6: Handling empty iterables with a default value
empty_list = []
max_value = max(empty_list, default="No items")  # Returns default if the list is empty
print("Maximum value:", max_value)  # Output: No items
```

```python
# Example 7: Finding the highest value in a dictionary by key comparison
grades = {"Alice": 90, "Bob": 85, "Charlie": 95}
top_student = max(grades, key=grades.get)  # Compares dictionary values
print("Top student:", top_student)  # Output: Charlie
```

```python
# Example 8: Using max to find the oldest person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 40), Person("Charlie", 35)]
oldest = max(people, key=lambda p: p.age)  # Finds the person with the largest age
print("Oldest person:", oldest.name)  # Output: Bob
```

```python
# Example 9: Comparing nested lists by their sum
nested_lists = [[1, 2], [3, 4], [5, 6]]
largest_sum_list = max(nested_lists, key=sum)  # Finds the list with the maximum sum
print("List with largest sum:", largest_sum_list)  # Output: [5, 6]
```

```python
# Example 10: Finding the largest squared number
numbers = [1, -2, 3, -4, 5]
max_square = max(numbers, key=lambda x: x**2)  # Compares numbers based on their square
print("Number with largest square:", max_square)  # Output: -4
```

```python
# Example 11: Finding the maximum number with duplicates
duplicates = [7, 7, 3, 5]
max_duplicate = max(duplicates)  # Finds the largest number
print("Maximum value:", max_duplicate)  # Output: 7
```
