"""
	Write a program to get the LCM of two positive integers. 
"""

def LCM(x, y):
    greater = max(x, y)
    lcm = greater

    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += greater

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"LCM of {num1} and {num2} is {LCM(num1, num2)}")
    
"""
	------- output 1 --------
    Enter the first number: 12
    Enter the second number: 15
    LCM of 12 and 15 is 60

	------- output 2 --------
    Enter the first number: 28
    Enter the second number: 14
    LCM of 28 and 14 is 28
"""