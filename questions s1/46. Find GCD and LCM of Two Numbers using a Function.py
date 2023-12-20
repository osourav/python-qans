"""
	Write a program to find GCD and LCM of two numbers by defining a function to compute GCD and LCM. 
"""

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    return (x * y) // compute_gcd(x, y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = compute_gcd(num1, num2)
lcm = compute_lcm(num1, num2)

print(f"GCD of {num1} and {num2} is {gcd}")
print(f"LCM of {num1} and {num2} is {lcm}")
    
"""
	------- output 1 --------
    Enter the first number: 12
    Enter the second number: 15
    GCD of 12 and 15 is 3
    LCM of 12 and 15 is 60

	------- output 2 --------
    Enter the first number: 4
    Enter the second number: 6
    GCD of 4 and 6 is 2
    LCM of 4 and 6 is 12
"""