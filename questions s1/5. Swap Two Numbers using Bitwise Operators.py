"""
   Write a program to swap two numbers using bitwise operators.
"""

a = 12
b = 10
print(f"Before swapping using bitwise operators: a = {a}, b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping using bitwise operators: a = {a}, b = {b}")


"""
   ------- output --------
   Before swapping using bitwise operators: a = 12, b = 10
   After swapping using bitwise operators: a = 10, b = 12
"""