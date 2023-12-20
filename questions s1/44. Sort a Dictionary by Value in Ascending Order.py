"""
	Write a program to sort (ascending order) a dictionary by value. 
"""

my_dect = {'apple': 30, 'banana': 15, 'cherry': 45, 'mango': 20}

sorted_dict = dict(sorted(my_dect.items(), key=lambda item: item[1]))
print("Unsorted Dictionary by:", my_dect)
print("Sorted Dictionary by Value:", sorted_dict)
    
"""
	------- output -------
    Unsorted Dictionary by: {'apple': 30, 'banana': 15, 'cherry': 45, 'mango': 20}
    Sorted Dictionary by Value: {'banana': 15, 'mango': 20, 'apple': 30, 'cherry': 45}
"""