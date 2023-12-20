"""
	Write a program to sort three numbers using if-elif-else. 
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 <= num3:
    sorted_nums = [num1, num2, num3]
elif num1 <= num3 <= num2:
    sorted_nums = [num1, num3, num2]
elif num2 <= num1 <= num3:
    sorted_nums = [num2, num1, num3]
elif num2 <= num3 <= num1:
    sorted_nums = [num2, num3, num1]
elif num3 <= num1 <= num2:
    sorted_nums = [num3, num1, num2]
else:
    sorted_nums = [num3, num2, num1]

print("Sorted Numbers:", sorted_nums)
    
"""
	------- output 1 --------
    Enter the first number: 5
    Enter the second number: 20
    Enter the third number: 10
    Sorted Numbers: [5.0, 10.0, 20.0]

	------- output 2 --------
    Enter the first number: 1 
    Enter the second number: 2
    Enter the third number: 3
    Sorted Numbers: [1.0, 2.0, 3.0]

	------- output 3 --------
    Enter the first number: 50
    Enter the second number: 25
    Enter the third number: 1
    Sorted Numbers: [1.0, 25.0, 50.0]
"""