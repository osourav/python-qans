"""
	Write a program to display unique and duplicate elements of a tuple. 
"""

inp = input("Enter a tuple of elements separated by spaces: ")
tuple_of_elements = tuple([x for x in inp.split()])

unique_elements = []
duplicate_elements = []
for element in set(tuple_of_elements):
    if tuple_of_elements.count(element) > 1:
        duplicate_elements.append(element)
    else:
        unique_elements.append(element)

print("Unique elements:", unique_elements)
print("Duplicate elements:", duplicate_elements)
    
"""
	------- output 1 --------
    Enter a tuple of elements separated by spaces: 1 2 3 4 2 5 6 4 7
    Unique elements: ['7', '1', '5', '6', '3']
    Duplicate elements: ['2', '4']

	------- output 2 --------
    Enter a tuple of elements separated by spaces: 5 10 25 10 11 22 10 7
    Unique elements: ['7', '25', '11', '5', '22']
    Duplicate elements: ['10']
"""