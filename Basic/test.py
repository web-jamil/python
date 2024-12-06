#filter even numbers from a list 
# nums=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)
# from functools import reduce
# nums=[1,2,3,4,5,6,7,8,9,10]
# product=reduce(lambda x,y:x*y,nums)
# print(product)

# add=lambda x,y=5:x+y
# print(add(3))
# print(add(3,10))


# nums=[1,2,3,4,5,6,7,8,9,10]
# square=[(lambda x:x**2) (x) for x in nums]
# print(square)
# def is_even(x):
#   return x%2==0
# evens=list(filter(is_even,range(10)))
# print(evens)
# reverse_string=lambda x:x[::-1]
# print(reverse_string("hello"))
# print(reverse_string("python"))
# print(reverse_string("world"))
# print(reverse_string("programming"))

# result=[x for x in range(10) if x%2==0]
# print(result)
# result=[x*2 for x in range(10)]
# print(result)
# format_string=lambda first,last:f"Name :{first} {last}"
# print(format_string("John","Doe"))

# formatter=lambda name,age:f"My name is {name} and I am {age} Years old.you live longer than you think {name}"
# print(formatter("Alice",25))

# grade=90
# if grade>= 65:
#   print("F")  

# num1,num2=10,20
# max=num1 if num1>num2 else num2
# if(num1<num2):
#   print("num1 is greater than num2")


# def password_Check(password):
#   if password=="Python@99":
#     print("Password is correct")
#   else:
#     print("Password is incorrect")
# password_Check("Python@99")
# password_Check("Python@98")
  
# hungry=True
# x="Feed the bear now!" if hungry else "Do not feed the bear"
# print(x)


# a=3
# print("A is positive") if a>0 else print("A is negative")


# num1,num2=10,20
# print("num1 is greater than num2") if num1>num2 else print("num2 is greater than num1")
# number=96
# if number>0: print("number is positive")
# else: print("number is negative")

# x=2
# if x>4:
#   print("x is greater than 4")
# else: 
#   print("x is less than 4")

# enter_age=int(input("Enter your age:"))
# year_require=0
# if enter_age>=18:
#   print("you are old enough to drive the car. to reach yout distination")
# else:
#   year_require=18-enter_age
#   print(f"you are not old enough to drive the car. you need {year_require} years to drive the car")


# my_year=int(input("Enter your year of birth:"))
# your_year=int(input("Enter your year of birth:"))
# if my_year==your_year:
#   print("My year is greater than your year")
# else:
#   difference=my_year-your_year
#   print(f"My year is greater than your year by {-difference} years")

# grade=96
# if grade>=90:
#   print("A Grade")
# elif grade>=80:
#   print("B Grade")
# elif grade>=70:
#   print("C Grade")
# elif grade>=60:
#   print("D Grade")
# else:
#   print("F Grade")

# student_grade=float(input("please enter your Grade :"))
# if student_grade>=90:
#   print(f"Your Grade is {student_grade} and you got A Grade")
# elif student_grade>=80:
#   print(f"Your Grade is {student_grade} and you got B Grade")
# elif student_grade>=70:
#   print(f"Your Grade is {student_grade} and you got C Grade")
# elif student_grade>=60:
#   print(f"Your Grade is {student_grade} and you got D Grade")
# else:
#   print(f"Your Grade is {student_grade} and you got F Grade")

# def user_check(choice):
#   if choice==1:
#     print("You have chosen option 1 and that means you are Admin")

#   elif choice==2:
#     print("You have chosen option 2 and that means you are User")
#   elif choice==3:
#     print("You have chosen option 3 and that means you are Guest")
#   else:
#     print("You have chosen invalid option")
 
# enter_choice=int(input("Enter your choice:"))
# user_check(enter_choice)

print("Welcome to Treasure Island .Your mission is to find the treasue ")
choice1=input("You are at a cross road. Where do you want to go? Type 'left' or 'right' ").lower().strip()
if choice1=="left":
  choice2=input("You come to a lake. There is a boat in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across ").lower().strip()
  if choice2=="wait":
    choice3=input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose? ").lower().strip()
    if choice3=="red":
      print("Game Over. You chose a door with a fire behind it")
    elif choice3=="yellow":
      print("You found the treasure! You Win!")
    elif choice3=="blue":
      print("Game Over. You chose a door with a fire behind it")
    else:
      print("You chose a door that does not exist. Game Over")
  else:
    print("Game Over. You got attacked by an angry trout")
else:
  print("Game Over. You fell into a hole")
  