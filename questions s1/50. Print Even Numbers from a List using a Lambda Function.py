"""
	Write a program to print the even numbers from a given list using the lambda function. 
"""

inp = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in inp.split()]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers in the list:", even_numbers)
    
"""
	------- output 1 --------
    Enter numbers separated by spaces: 10 11 12 13 15 16
    Even numbers in the list: [10, 12, 16]
     
	------- output 2 --------
    Enter numbers separated by spaces: 1 2 3 4 5 6
    Even numbers in the list: [2, 4, 6]
"""