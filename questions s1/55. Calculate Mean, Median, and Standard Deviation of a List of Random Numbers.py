"""
	Write a program to find the mean, median, and standard deviation of a list of random numbers between 1 and 10. 
"""

import statistics
import random

random_numbers = [random.randint(1, 10) for _ in range(10)]

mean = statistics.mean(random_numbers)
median = statistics.median(random_numbers)
std_dev = statistics.stdev(random_numbers)

print(f"List of random numbers: {random_numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
    
"""
	------- output 1 --------
	List of random numbers: [4, 9, 2, 3, 5, 2, 7, 9, 3, 1]
	Mean: 4.5
	Median: 3.5
	Standard Deviation: 2.9154759474226504

	------- output 2 --------
	List of random numbers: [2, 4, 2, 9, 8, 3, 6, 4, 6, 2]
	Mean: 4.6
	Median: 4.0
	Standard Deviation: 2.5473297566057065
"""