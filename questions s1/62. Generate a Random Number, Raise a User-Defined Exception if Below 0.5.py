"""
	Write a program to generate a random number. Raise a user-defined exception if the number is below 0.5. 
"""

import random

class BelowThresholdError(Exception):
    def __init__(self, value):
        super().__init__(f"Error: Random number {value:.6f} is below 0.5")

try:
    random_number = random.random()
    if random_number < 0.5:
        raise BelowThresholdError(random_number)
    else:
        print(f"Random number is: {random_number:.6f}")

except BelowThresholdError as e:
    print(e)
    
"""
	------- output 1 --------
    Random number is: 0.569994

	------- output 2 --------
    Error: Random number 0.498421 is below 0.5
"""