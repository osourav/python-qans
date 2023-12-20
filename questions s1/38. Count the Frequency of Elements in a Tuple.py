"""
	Write a program to count the frequency of all the elements in a tuple. 
"""

inp = input("Enter a tuple of elements separated by spaces: ")
tuple_of_elements = tuple([x for x in inp.split()])

element_frequency = {}
for element in set(tuple_of_elements):
    element_frequency[element] = tuple_of_elements.count(element)

print("input tuple:", tuple_of_elements)
print("Frequency of elements in the tuple:", element_frequency)
    
"""
	------- output 1 --------
    Enter a tuple of elements separated by spaces: a b c d b a e f e
    input tuple: ('a', 'b', 'c', 'd', 'b', 'a', 'e', 'f', 'e')
    Frequency of elements in the tuple: {'c': 1, 'd': 1, 'e': 2, 'b': 2, 'f': 1, 'a': 2}

	------- output 2 --------
    Enter a tuple of elements separated by spaces: 1 2 5 3 1 4 3
    input tuple: ('1', '2', '5', '3', '1', '4', '3')
    Frequency of elements in the tuple: {'2': 1, '3': 2, '1': 2, '4': 1, '5': 1}
"""