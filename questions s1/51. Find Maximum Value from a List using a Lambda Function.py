"""
	Write a program to find the maximum value from a list using the lambda function. 
"""

inp = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in inp.split()]

max_value = max(numbers, key=lambda x: x)
print("Maximum value in the list:", max_value)
    
"""
	------- output 1 --------
    Enter numbers separated by spaces: 25 50 10 20
    Maximum value in the list: 50

	------- output 2 --------
    Enter numbers separated by spaces: 1 2 3 4 8 5 6 7
    Maximum value in the list: 8
"""
