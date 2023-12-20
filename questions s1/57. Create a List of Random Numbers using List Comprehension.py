"""
	Write a program to create a list of random numbers using list comprehension. 
"""

import random
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))
list_size = int(input("Enter list size: "))
random_numbers = [random.randint(lower_limit, upper_limit) for _ in range(list_size)]

print(f"List of random numbers using list comprehension: {random_numbers}")

"""
	------- output 1 --------
	Enter lower limit: 1
	Enter upper limit: 100 
	Enter list size: 12
	List of random numbers using list comprehension: [45, 69, 53, 63, 10, 50, 94, 57, 49, 55, 83, 56]

	------- output 2 --------
	Enter lower limit: 10 
	Enter upper limit: 15
	Enter list size: 8 
	List of random numbers using list comprehension: [10, 13, 14, 12, 11, 14, 13, 10]
"""