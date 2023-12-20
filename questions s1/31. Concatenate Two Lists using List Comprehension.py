"""
	Write a program to concatenate two lists using list comprehension. 
"""

inp1 = input("Enter the first list of numbers separated by spaces: ")
inp2 = input("Enter the second list of numbers separated by spaces: ")

list1 = [x for x in inp1.split()]
list2 = [x for x in inp2.split()]

concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

"""
	------- output 1 --------
    Enter the first list of numbers separated by spaces: 10 20 30 50
    Enter the second list of numbers separated by spaces: a b c d
    Concatenated list: ['10', '20', '30', '50', 'a', 'b', 'c', 'd']

	------- output 2 --------
    Enter the first list of numbers separated by spaces: x y z
    Enter the second list of numbers separated by spaces: 3 2 1
    Concatenated list: ['x', 'y', 'z', '3', '2', '1']
"""