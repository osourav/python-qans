"""
	Write a program to rotate the values of x, y, and z such that x has the value of y, y has the value of z, and z has the value of x. 
"""

x, y, z = 5, 10, 15
print(f"Before rotate values: x = {x}, y = {y}, z = {z}")
x, y, z = y, z, x
print(f"After rotated values: x = {x}, y = {y}, z = {z}")

"""
	------- output 1 --------
	Before rotate values: x = 1, y = 2, z = 3
	After rotated values: x = 2, y = 3, z = 1

	------- output 2 --------
	Before rotate values: x = 5, y = 10, z = 15
	After rotated values: x = 10, y = 15, z = 5
"""
