"""
	Write a program to read a number from the user and print its square. Generate KeyboardInterrupt exception if Ctrl + C is pressed instead of a number. 
"""


try:
    number = float(input("Enter a number: "))
    square = number ** 2
    print(f"The square of {number} is: {square}")
except KeyboardInterrupt:
    print("Ctrl + C detected. Exiting the program.")
    
"""
	------- output 1 --------
    Enter a number: 6
    The square of 6.0 is: 36.0

	------- output 2 --------
    Enter a number: Ctrl + C detected. Exiting the program.
"""