# ================================
# Python Sets: All About Syntaxes
# ================================

# ========== 1. Set Basics ==========
# Creating sets
set1 = {1, 2, 3, 4}
set2 = set([4, 5, 6])  # From a list
empty_set = set()      # Empty set (note: {} creates a dict)

print("Set 1:", set1)             # Output: {1, 2, 3, 4}
print("Set 2:", set2)             # Output: {4, 5, 6}
print("Empty Set:", empty_set)    # Output: set()

# Sets automatically remove duplicates
set_with_duplicates = {1, 2, 2, 3}
print("No Duplicates:", set_with_duplicates)  # Output: {1, 2, 3}

# ========== 2. Adding/Removing Elements ==========
# Adding elements
set1.add(5)
print("After add:", set1)  # Output: {1, 2, 3, 4, 5}

# Adding multiple elements
set1.update([6, 7])
print("After update:", set1)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Removing elements
set1.remove(7)   # Removes 7; raises KeyError if not found
set1.discard(8)  # Does nothing if 8 is not in the set
print("After remove/discard:", set1)  # Output: {1, 2, 3, 4, 5, 6}

# Pop an arbitrary element
popped = set1.pop()
print("Popped element:", popped)
print("After pop:", set1)

# Clear the set
set1.clear()
print("After clear:", set1)  # Output: set()

# ========== 3. Set Operations ==========
a = {1, 2, 3}
b = {3, 4, 5}

# Union
union_set = a | b
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = a & b
print("Intersection:", intersection_set)  # Output: {3}

# Difference
difference_set = a - b
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference
sym_diff = a ^ b
print("Symmetric Difference:", sym_diff)  # Output: {1, 2, 4, 5}

# ========== 4. Subset and Superset ==========
small_set = {1, 2}
large_set = {1, 2, 3, 4}

# Subset check
print("Is subset:", small_set.issubset(large_set))  # True
print("Is subset (operator):", small_set <= large_set)  # True

# Superset check
print("Is superset:", large_set.issuperset(small_set))  # True
print("Is superset (operator):", large_set >= small_set)  # True

# Disjoint sets
disjoint = {5, 6}
print("Is disjoint:", small_set.isdisjoint(disjoint))  # True

# ========== 5. Copying ==========
copy_set = large_set.copy()
print("Copied set:", copy_set)  # Output: {1, 2, 3, 4}

# ========== 6. Membership Testing ==========
print(1 in large_set)   # Output: True
print(5 not in large_set)  # Output: True

# ========== 7. Iterating Over a Set ==========
for element in large_set:
    print("Element:", element)

# ========== 8. Set Comprehensions ==========
squared_set = {x**2 for x in range(5)}
print("Set Comprehension:", squared_set)  # Output: {0, 1, 4, 9, 16}

# ========== 9. Frozen Sets ==========
# Frozen sets are immutable versions of sets
frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)
# frozen.add(4)  # Error: 'frozenset' object has no attribute 'add'

# Frozen sets support operations
print("Frozen Union:", frozen | {4})  # Output: frozenset({1, 2, 3, 4})

# ========== 10. Advanced Usage ==========
# Using `len` for size
print("Set size:", len(a))  # Output: 3

# Using `set()` to remove duplicates from a list
dupes = [1, 2, 2, 3, 4, 4]
unique_set = set(dupes)
print("Unique Set:", unique_set)  # Output: {1, 2, 3, 4}

# Using sets for intersection in lists
list1 = [1, 2, 3]
list2 = [2, 3, 4]
common_elements = set(list1) & set(list2)
print("Common Elements:", common_elements)  # Output: {2, 3}
