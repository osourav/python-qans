"""
	Write a program to find the union of two lists. 
"""

inp1 = input("Enter the first list of numbers separated by spaces: ")
inp2 = input("Enter the second list of numbers separated by spaces: ")

list1 = [int(x) for x in inp1.split()]
list2 = [int(x) for x in inp2.split()]

union_list = list(set(list1) | set(list2))
print("Union of the two lists:", union_list)
    
"""
	------- output -------
    Enter the first list of numbers separated by spaces: 10 12 15 10 5
    Enter the second list of numbers separated by spaces: 30 10 12 5
    Union of the two lists: [5, 10, 12, 15, 30]
"""