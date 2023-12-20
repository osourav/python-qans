"""
	Write a program to find all the unique elements of a list by defining a function. 
"""

def find_unique_elements(input_list):
    return list(set(input_list))

inp = input("Enter numbers separated by spaces: ")
numbers = [x for x in inp.split()]
unique_elements = find_unique_elements(numbers)

print("Unique elements in the list:", unique_elements)
    
"""
	------- output 1 --------
    Enter numbers separated by spaces: a b c d b d e f
    Unique elements in the list: ['c', 'f', 'b', 'e', 'd', 'a']

	------- output 2 --------
    Enter numbers separated by spaces: 10 20 15 20 5 10 12
    Unique elements in the list: ['12', '10', '20', '15', '5']
"""