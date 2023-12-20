"""
	Write a program to merge two dictionaries. 
"""

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

merged_dict = {**dict1, **dict2}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)
    
"""
	------- output -------
    Dictionary 1: {'a': 1, 'b': 2, 'c': 3}
    Dictionary 2: {'d': 4, 'e': 5, 'f': 6}
    Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
"""