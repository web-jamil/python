# Basic Example: Sum of a list
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)  # Adds all elements in the list: 1 + 2 + 3 + 4 + 5
print(result)  # Output: 15

# Using the 'start' parameter
result_with_start = sum(numbers, 10)  # Adds 10 to the sum of the list: 10 + (1 + 2 + 3 + 4 + 5)
print(result_with_start)  # Output: 25

# Summing elements from a range
range_sum = sum(range(1, 11))  # Adds numbers from 1 to 10
print(range_sum)  # Output: 55

# Using a generator expression to filter elements
even_sum = sum(x for x in numbers if x % 2 == 0)  # Sum only the even numbers in the list
print(even_sum)  # Output: 6 (2 + 4)

# Summing complex numbers
complex_numbers = [1 + 2j, 3 + 4j, 5 + 6j]
complex_sum = sum(complex_numbers)  # Adds all complex numbers
print(complex_sum)  # Output: (9+12j)

# Summing the values in a dictionary
data = {"Alice": 95, "Bob": 85, "Charlie": 75}
total_score = sum(data.values())  # Extracts the scores and sums them: 95 + 85 + 75
print(total_score)  # Output: 255

# Summing rows in a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sums = [sum(row) for row in matrix]  # Computes the sum of each row
print(row_sums)  # Output: [6, 15, 24]

# Summing columns in a matrix
column_sums = [sum(col) for col in zip(*matrix)]  # Transposes the matrix and sums each column
print(column_sums)  # Output: [12, 15, 18]

# Handling an empty iterable with the 'start' parameter
empty_sum = sum([], start=5)  # Default sum is 0; start value is added
print(empty_sum)  # Output: 5
