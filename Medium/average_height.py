students_heights=input("Input a list of student heights ").split()

for n in range(len(students_heights)):
  students_heights[n]=int(students_heights[n])
print(students_heights)
total_height=0
for height in students_heights:
    total_height+=height
    
print(total_height)
# total_height=sum(students_heights)
number_of_students=0
for student in students_heights:
   number_of_students+=1
print(number_of_students)
# number_of_students=len(students_heights)
average_height=round(total_height/number_of_students)
print(average_height)


# Input heights as a space-separated string and convert it into a list of strings
students_heights = input("Input a list of student heights ").split()

# Convert the string list to integers
for n in range(len(students_heights)):
    students_heights[n] = int(students_heights[n])

# Initialize total_height to 0
total_height = 0
print(type(students_heights[0]))
# Manually sum the heights using a loop
for height in students_heights:
    total_height += height

# Print the total height
print(total_height)






# data = [
#     {"name": "Alice", "score": 95},
#     {"name": "Bob", "score": 85},
#     {"name": "Charlie", "score": 75}
# ]
# total_score = sum(d["score"] for d in data)
# print(total_score)  # Output: 255

