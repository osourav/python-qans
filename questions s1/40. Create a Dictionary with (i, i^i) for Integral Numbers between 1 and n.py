"""
	Write a program to create a dictionary that contains (i, i^2) such that i is an integral number between 1 and n (both included). 
"""

n = int(input("Enter the value of n: "))
squared_dict = {i: i * i for i in range(1, n + 1)}
print("Dictionary:", squared_dict)
    
"""
	------- output 1 --------
    Enter the value of n: 10
    Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

	------- output 2 --------
    Enter the value of n: 15
    Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""