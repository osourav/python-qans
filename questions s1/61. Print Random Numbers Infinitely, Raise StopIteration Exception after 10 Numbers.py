"""
	Write a program to print random numbers infinitely. Raise the StopIteration exception after displaying 10 numbers to exit from the program. 
"""

import random

class InfiniteRandomNumbers:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < 10:
            self.count += 1
            return random.randint(1, 100)
        else:
            raise StopIteration

infinite_numbers = InfiniteRandomNumbers()

print("Random numbers: ", end="")
for num in infinite_numbers:
    print(num, end=", ")

"""
	------- output 1 --------
    Random numbers: 30, 4, 41, 10, 86, 84, 51, 10, 60, 65,

	------- output 2 --------
    Random numbers: 65, 46, 97, 13, 62, 32, 32, 100, 73, 98,
"""