"""
	Write a program to create a list from two given lists 'list1' and 'list2' of numbers such that it contains numbers that are present in 'list2' but not in 'list1'. 
"""

inp1 = input("Enter the first list of numbers separated by spaces: ")
inp2 = input("Enter the second list of numbers separated by spaces: ")

list1 = [int(x) for x in inp1.split()]
list2 = [int(x) for x in inp2.split()]

unique_list = list(set(list2) - set(list1))
print("List containing numbers present in 'list2' but not in 'list1':", unique_list)
    
"""
	------- output 1 --------
    Enter the first list of numbers separated by spaces: 1 2 3 4 5 6
    Enter the second list of numbers separated by spaces: 3 4 5 6 7 8
    List containing numbers present in 'list2' but not in 'list1': [8, 7]

	------- output 2 --------
    Enter the first list of numbers separated by spaces: 10 20 30 
    Enter the second list of numbers separated by spaces: 30 40 50 60
    List containing numbers present in 'list2' but not in 'list1': [40, 50, 60]
"""