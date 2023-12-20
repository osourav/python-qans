"""
	Write a program to compute the GCD of two integer numbers. 
"""

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = compute_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")
    
"""
	------- output 1 --------
    Enter the first number: 20
    Enter the second number: 28
    GCD of 20 and 28 is 4

	------- output 2 --------
    Enter the first number: 100
    Enter the second number: 25
    GCD of 100 and 25 is 25
"""