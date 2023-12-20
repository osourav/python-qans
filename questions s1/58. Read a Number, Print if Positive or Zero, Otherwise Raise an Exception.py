"""
	Write a program to read a number from the user. If the number is positive or zero, print it; otherwise, raise an exception. 
"""

try:
    number = float(input("Enter a number: "))
    if number >= 0:
        print(f"The number is: {number}")
    else:
        raise ValueError("Number should be positive or zero.")
except ValueError as ve:
    print(f"Error: {ve}")
    
"""
	------- output 1 --------
    Enter a number: -1
    Error: Number should be positive or zero.

	------- output 2 --------
    Enter a number: 2
    The number is: 2.0
"""