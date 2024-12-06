# Example 1: Slicing a List
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing from index 2 to 5 (exclusive)
sliced_list = my_list[2:5]
print("Sliced List (2:5):", sliced_list)  # Output: [2, 3, 4]

# Slicing the entire list with a step of 2 (every second element)
sliced_list_with_step = my_list[::2]
print("Sliced List (every second element):", sliced_list_with_step)  # Output: [0, 2, 4, 6, 8]

# Slicing with negative indices to get the last three elements
last_three = my_list[-3:]
print("Last three elements:", last_three)  # Output: [7, 8, 9]


# Example 2: Slicing a String
my_string = "Hello, World!"

# Slicing from index 7 to the end of the string
sliced_string = my_string[7:]
print("Sliced String (from index 7):", sliced_string)  # Output: "World!"

# Slicing the string to get every third character
sliced_string_with_step = my_string[::3]
print("Sliced String (every third character):", sliced_string_with_step)  # Output: "Hl r!"


# Example 3: Slicing a Tuple
my_tuple = (10, 20, 30, 40, 50)

# Slicing from index 1 to 3 (exclusive)
sliced_tuple = my_tuple[1:3]
print("Sliced Tuple (1:3):", sliced_tuple)  # Output: (20, 30)


# Example 4: Using the `slice` Function
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a slice object that slices from index 2 to 8 with a step of 2
slice_obj = slice(2, 8, 2)

# Use the slice object to slice the list
sliced_list_with_slice_obj = my_list[slice_obj]
print("Sliced List using slice object (2:8:2):", sliced_list_with_slice_obj)  # Output: [2, 4, 6]


# Example 5: Slicing with Negative Indices
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Slicing to get elements from index -5 to -1 (last five elements)
sliced_negative_indices = my_list[-5:-1]
print("Sliced List with Negative Indices (-5:-1):", sliced_negative_indices)  # Output: [50, 60, 70, 80]

# Slicing the entire list in reverse order
reversed_list = my_list[::-1]
print("Reversed List:", reversed_list)  # Output: [90, 80, 70, 60, 50, 40, 30, 20, 10]


# Example 6: Slicing with Step
my_string = "abcdefghij"

# Slicing with a negative step to reverse the string
reversed_string = my_string[::-1]
print("Reversed String:", reversed_string)  # Output: "jihgfedcba"

# Slicing to get every second character in reverse order
every_second_reversed = my_string[::-2]
print("Every second character in reverse:", every_second_reversed)  # Output: "jhfdb"


# Example 7: Combining Slicing
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Combining slicing to get elements from index 1 to 7 with a step of 2
combined_slicing = my_list[1:8:2]
print("Combined Slicing (1:8:2):", combined_slicing)  # Output: [2, 4, 6, 8]

squares=[x*x for x in range(6)]
print(squares)

list=[1,-2,3,4,5,6,7,-8,9,-10]
new_list=sorted(list)
my_list.sort(reverse=True)
print(my_list)
print(new_list)
even_squares=[x*x for x in range(10) if x%2==0]
print(even_squares)