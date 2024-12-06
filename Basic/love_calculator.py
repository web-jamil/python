print("Welcome to the love calcultaor! and here you can find the love percentage between two people by entering their names below.")
name1=input("Enter your name: ")
name1=name1.lower()
name2=input("Enter your partner's name: ")
name2=name2.lower()
comnbined_name=name1+name2
t=comnbined_name.count('t')
r=comnbined_name.count('r')
u=comnbined_name.count('u')
e=comnbined_name.count('e')

true=t+r+u+e


e=comnbined_name.count('e')
o=comnbined_name.count('o')
v=comnbined_name.count('v')
l=comnbined_name.count('l')
love=l+o+v+e
total=str(true)+str(love)
print(f"Your love percentage is: {total}%")


if  int(total)<90 or int(total)< 10 :
    print(f"Your score is {total}, you go together like coke and mentos.")
elif int(total)>=40 and int(total)<=50:
    print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total} % and your love percentage is too low .")