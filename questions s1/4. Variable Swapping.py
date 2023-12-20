"""
   Write a program to swap the value of two variables using a third variable and without using a third variable
"""

# Using a third variable
a = 5
b = 10
print(f"Before swapping (with third variable): a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After swapping (with third variable): a = {a}, b = {b}")

# Without using a third variable
a = 15
b = 1
print(f"Before swapping (without third variable): a = {a}, b = {b}")
a, b = b, a
print(f"After swapping (without third variable): a = {a}, b = {b}")

"""
   ------- output --------
   Before swapping (with third variable): a = 5, b = 10
   After swapping (with third variable): a = 10, b = 5
   Before swapping (without third variable): a = 15, b = 1
   After swapping (without third variable): a = 1, b = 15
"""