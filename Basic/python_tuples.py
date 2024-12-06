# ================================
# Python Tuples: All About Syntaxes
# ================================

# ========== 1. Tuple Basics ==========
# Creating tuples
empty_tuple = ()
single_element_tuple = (1,)  # Note the trailing comma for single-element tuple
multi_element_tuple = (1, 2, 3)
tuple_with_mixed_types = (1, "hello", 3.14)

print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Multi-Element Tuple:", multi_element_tuple)
print("Mixed Type Tuple:", tuple_with_mixed_types)

# Creating a tuple without parentheses
implicit_tuple = 1, 2, 3
print("Implicit Tuple:", implicit_tuple)

# Tuple length
print("Length of Tuple:", len(multi_element_tuple))

# ========== 2. Accessing Tuple Elements ==========
# Indexing
print("First Element:", multi_element_tuple[0])
print("Last Element:", multi_element_tuple[-1])

# Slicing
print("Subtuple (0-2):", multi_element_tuple[:2])

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print("Nested Tuple Element (1):", nested_tuple[1])
print("Accessing Nested Element:", nested_tuple[1][1])  # Output: 3

# ========== 3. Tuple Immutability ==========
# Tuples are immutable, so you can't change elements
try:
    multi_element_tuple[0] = 99  # Raises TypeError
except TypeError as e:
    print("Error:", e)

# However, mutable objects within tuples can be modified
mutable_inside_tuple = (1, [2, 3], 4)
mutable_inside_tuple[1][0] = 99  # Modifies the list inside the tuple
print("Modified Tuple with Mutable Elements:", mutable_inside_tuple)

# ========== 4. Tuple Operations ==========
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

# Membership testing
print("Is 2 in tuple1?", 2 in tuple1)
print("Is 5 not in tuple1?", 5 not in tuple1)

# Iteration
for element in multi_element_tuple:
    print("Tuple Element:", element)

# ========== 5. Tuple Methods ==========
# Counting occurrences
example_tuple = (1, 2, 2, 3, 4, 2)
print("Count of 2:", example_tuple.count(2))

# Finding index
print("Index of 3:", example_tuple.index(3))

# ========== 6. Packing and Unpacking Tuples ==========
# Tuple packing
packed_tuple = 1, 2, 3
print("Packed Tuple:", packed_tuple)

# Tuple unpacking
a, b, c = packed_tuple
print("Unpacked Values: a =", a, ", b =", b, ", c =", c)

# Swapping variables using tuples
x, y = 10, 20
x, y = y, x
print("Swapped Variables: x =", x, ", y =", y)

# Unpacking with the splat operator (*)
tuple_with_rest = (1, 2, 3, 4, 5)
first, *rest = tuple_with_rest
print("First Element:", first)
print("Rest of the Elements:", rest)

# Unpacking nested tuples
nested = (1, (2, 3), 4)
_, (a, b), _ = nested
print("Unpacked Nested Elements: a =", a, ", b =", b)

# ========== 7. Advanced Tuple Operations ==========
# Tuples as dictionary keys (since they are hashable)
tuple_key_dict = {("key1", "key2"): "value"}
print("Value for Tuple Key:", tuple_key_dict[("key1", "key2")])

# Comparing tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print("Is tuple1 < tuple2?", tuple1 < tuple2)  # Lexicographical comparison

# Converting between tuples and other data types
list_to_tuple = tuple([1, 2, 3])
print("Converted List to Tuple:", list_to_tuple)

tuple_to_list = list((1, 2, 3))
print("Converted Tuple to List:", tuple_to_list)

# Using `zip()` to create tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print("Zipped Tuples:", list(zipped))

# ========== 8. Performance Considerations ==========
import sys

# Memory efficiency
large_list = list(range(1000))
large_tuple = tuple(range(1000))
print("Size of List (bytes):", sys.getsizeof(large_list))
print("Size of Tuple (bytes):", sys.getsizeof(large_tuple))

# ========== 9. Common Use Cases ==========
# Returning multiple values from a function
def calculate(a, b):
    return a + b, a * b  # Returns a tuple

sum_result, product_result = calculate(5, 10)
print("Sum:", sum_result, ", Product:", product_result)

# Tuples as fixed records
coordinates = (10.0, 20.0)  # A fixed point in space
print("Coordinates:", coordinates)

# Iterating over a list of tuples
students = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]
for name, score in students:
    print(f"Student: {name}, Score: {score}")

# ========== 10. Tuple Comprehensions? ==========
# Tuples do not have comprehensions, but you can create them from lists
tuple_comp = tuple(x for x in range(10) if x % 2 == 0)
print("Tuple Comprehension Equivalent:", tuple_comp)

