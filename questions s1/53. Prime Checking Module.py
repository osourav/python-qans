"""
	Create a module to check whether a number is a prime or not. Write a program to find the prime number between two limits using this module. 
"""

from prime_module import is_prime

lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

print(f"Prime numbers between {lower_limit} and {upper_limit}:")
for num in range(lower_limit, upper_limit + 1):
    if is_prime(num):
        print(num, end=", ")
    
"""
	------- output 1 --------
    Enter lower limit: 1
    Enter upper limit: 20
    Prime numbers between 1 and 20:
    2, 3, 5, 7, 11, 13, 17, 19,

	------- output 2 --------
    Enter lower limit: 5
    Enter upper limit: 30
    Prime numbers between 5 and 30:
    5, 7, 11, 13, 17, 19, 23, 29,
"""