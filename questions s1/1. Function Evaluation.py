"""
   Write a program to find the value of the function :
   F(x)=3x2+5   if x<= 10
       =5x      if x>10 and x<=20
       =2x2-x+9 if x>20

 Input value of x .
"""

x = float(input("Enter the value of x: "))

if x <= 10:
    result = 3 * x**2 + 5
elif 10 < x <= 20:
    result = 5 * x
else:
    result = 2 * x**2 - x + 9

print(f"The result of the function for x = {x} is: {result}")

"""
   ------- output 1 --------
   Enter the value of x: 10
   The result of the function for x = 10.0 is: 305.0

   ------- output 2 --------
   Enter the value of x: 15
   The result of the function for x = 15.0 is: 75.0

   ------- output 3 --------
   Enter the value of x: 30
   The result of the function for x = 30.0 is: 1779.0
"""
