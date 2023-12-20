"""
	Write a program to display the following numbers: 5678, 678, 78, 8, where the given number is 5678. 
"""

number = 5678
print("Numbers:", end=" ")
for i in range(len(str(number)), 0, -1):
    print(number % 10 ** i, end=", ")

"""
	------- output --------
    Numbers: 5678, 678, 78, 8,

"""