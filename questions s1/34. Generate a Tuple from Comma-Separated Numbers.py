"""
	Write a program to accept a sequence of comma-separated numbers from the user and generate a tuple with those numbers. 
"""

inp = input("Enter a sequence of comma-separated numbers: ")
my_list = [int(x) for x in inp.split(",")]
my_tuple = tuple(my_list)

print("Input Numbers:", my_tuple)
    
"""
	------- output 1 --------
    Enter a sequence of comma-separated numbers: 10,20,30,40
    Input Numbers: (10, 20, 30, 40)

	------- output 2 --------
    Enter a sequence of comma-separated numbers: 5,10,15,20
    Input Numbers: (5, 10, 15, 20)
"""