def recursion_factorial(a):
   if a == 1:
       return a
   else:
       return a*recursion_factorial(a-1)
number = 7

# control  if the number is negative
if number < 0:
   print("Error, factorial does not exist for negative numbers")
elif number == 0:
   print("For 0 factorial is 1")
else:
   print(f"The factorial of {number} is {recursion_factorial(number)}")

