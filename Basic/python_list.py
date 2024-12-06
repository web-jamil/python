# Example 1: Creating a List
# Creating a list of integers
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)  # Output: [1, 2, 3, 4, 5]


# Example 2: Accessing Elements
# Accessing elements using indexing
first_element = my_list[0]  # First element (index 0)
last_element = my_list[-1]   # Last element (negative index)
print("First Element:", first_element)  # Output: 1
print("Last Element:", last_element)    # Output: 5


# Example 3: Adding Elements
# Adding elements using append() method
my_list.append(6)  # Adds 6 to the end of the list
print("After Append:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Adding multiple elements using extend() method
my_list.extend([7, 8])  # Adds 7 and 8 to the end of the list
print("After Extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# Example 4: Inserting Elements
# Inserting an element at a specific index using insert() method
my_list.insert(0, 0)  # Inserts 0 at index 0
print("After Insert:", my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Example 5: Removing Elements
# Removing an element using remove() method
my_list.remove(4)  # Removes the first occurrence of 4
print("After Remove:", my_list)  # Output: [0, 1, 2, 3, 5, 6, 7, 8]

# Removing the last element using pop() method
last_item = my_list.pop()  # Removes and returns the last element
print("After Pop:", my_list)  # Output: [0, 1, 2, 3, 5, 6, 7]
print("Popped Item:", last_item)  # Output: 8


# Example 6: Slicing a List
# Slicing the list to get a subset of elements
sliced_list = my_list[1:4]  # Gets elements from index 1 to 3 (exclusive)
print("Sliced List (1:4):", sliced_list)  # Output: [1, 2, 3]

# Slicing with step
sliced_with_step = my_list[::2]  # Gets every second element
print("Sliced List (Every Second Element):", sliced_with_step)  # Output: [0, 2, 5]


# Example 7: List Comprehensions
# Creating a new list using list comprehension
squared_numbers = [x**2 for x in range(5)]  # Squares of numbers 0 to 4
print("Squared Numbers:", squared_numbers)  # Output: [0, 1, 4, 9, 16]


# Example 8: Sorting a List
# Sorting the list in ascending order using sort() method
my_list.sort()  # Sorts the list in place
print("Sorted List:", my_list)  # Output: [0, 1, 2, 3, 5, 6, 7]

# Sorting in descending order
my_list.sort(reverse=True)  # Sorts the list in place in descending order
print("Sorted List (Descending):", my_list)  # Output: [7, 6, 5, 3, 2, 1, 0]


# Example 9: Reversing a List
# Reversing the list in place using reverse() method
my_list.reverse()
print("Reversed List:", my_list)  # Output: [0, 1, 2, 3, 5, 6, 7] (if sorted)


# Example 10: Finding Length of a List
# Getting the number of elements in the list using len() function
length_of_list = len(my_list)
print("Length of List:", length_of_list)  # Output: 7 (or the current length)


# Example 11: Checking Membership
# Checking if an element is in the list using 'in' keyword
is_present = 3 in my_list
print("Is 3 in the List?", is_present)  # Output




s = " Hello   World "
print(s.replace(" ", ""))  # Output: "HelloWorld"
