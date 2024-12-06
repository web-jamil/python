def calculator(a,b,operation="add"):
  if operation=="add":
    return a+b
  elif operation=="subtract":
    return a-b
  elif operation=="multiply":
    return a*b
  elif operation=="divide":
    return a/b
  elif operation=="remainder":
    return a%b
  elif operation=="exponent":
    return a**b
  elif operation=="floor_division":
    return a//b
  else:
    return "Invalid operation"
print(calculator(5,2,"remainder"))
print(calculator(5,2,"floor_division"))