"""
	Write a program to read the age of a person and raise exceptions if age is negative. 
"""

class NegativeAgeError(Exception):
    def __init__(self):
        super().__init__("Error: Age cannot be negative")

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAgeError()
    else:
        print(f"Your age is: {age}")

except NegativeAgeError as e:
    print(e)
    
"""
	------- output 1 --------
    Enter your age: 22
    Your age is: 22

	------- output 2 --------
    Enter your age: -20
    Error: Age cannot be negative
"""