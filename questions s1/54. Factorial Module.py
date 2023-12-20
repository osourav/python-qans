"""
	Create a module to find the factorial of a number and import the module from the main program to find the factorial of a given number. 
"""

from factorial_module import factorial

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
    
"""
	------- output 1 --------
    Enter a number: 6
    The factorial of 6 is: 720

	------- output 2 --------
    Enter a number: 4
    The factorial of 4 is: 24
"""