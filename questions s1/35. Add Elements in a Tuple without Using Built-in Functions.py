"""
	Write a program to add elements in a tuple without using built-in functions. 
"""

def tuple_sum(my_tuple):
    sum = 0
    for x in list(my_tuple):
        sum += x
    return sum


inp = input("Enter a tuple of integers separated by spaces: ")
input_list = [int(x) for x in inp.split()]
tuple_of_integers = tuple(input_list)

print(f"input tuple elements: {tuple_of_integers}")
print(f"Sum of elements in the tuple: {tuple_sum(tuple_of_integers)}")
    
"""
	------- output 1 --------
    Enter a tuple of integers separated by spaces: 5 10 15 20
    input tuple elements: (5, 10, 15, 20)
    Sum of elements in the tuple: 50

	------- output 2 --------
    Enter a tuple of integers separated by spaces: 1 2 3 4 5 6
    input tuple elements: (1, 2, 3, 4, 5, 6)
    Sum of elements in the tuple: 21

"""