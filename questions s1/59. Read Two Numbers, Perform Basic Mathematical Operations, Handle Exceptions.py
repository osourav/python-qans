"""
	Write a program to read two numbers from the user and perform basic mathematical operations (addition, multiplication, subtraction, division) by handling all possible exceptions. 
"""

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result_addition = num1 + num2
    result_subtraction = num1 - num2
    result_multiplication = num1 * num2
    result_division = num1 / num2

    print(f"Addition: {result_addition}")
    print(f"Subtraction: {result_subtraction}")
    print(f"Multiplication: {result_multiplication}")
    print(f"Division: {result_division}")

except Exception as e:
    print(f"Error: {e}")
    
"""
	------- output 1 --------
    Enter the first number: 2
    Enter the second number: 3
    Addition: 5.0
    Subtraction: -1.0
    Multiplication: 6.0
    Division: 0.6666666666666666

	------- output 2 --------
    Enter the first number: 5
    Enter the second number: 0
    Error: float division by zero
"""