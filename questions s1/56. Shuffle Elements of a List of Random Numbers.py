"""
	Write a program to shuffle elements of a list of random numbers between given ranges. 
"""

import random

lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))
random_numbers = list(range(lower_limit, upper_limit))
random.shuffle(random_numbers)

print(f"Shuffled list: {random_numbers}")
    
"""
	------- output 1 --------
	Enter lower limit: 1
	Enter upper limit: 10 
	Shuffled list: [3, 8, 9, 7, 2, 5, 1, 6, 4]

	------- output 2 --------
	Enter lower limit: 5
	Enter upper limit: 15
	Shuffled list: [8, 12, 6, 10, 9, 13, 7, 14, 11, 5]
"""