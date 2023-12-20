"""
	Write a program to calculate the mean of elements in a tuple of integers. 
"""

def tuple_mean(my_tuple):
    if len(my_tuple) > 0:
        sum = 0
        for x in list(my_tuple):
            sum += x
        return sum / len(my_tuple)
    return 0


inp = input("Enter a tuple of integers separated by spaces: ")
input_list = [int(x) for x in inp.split()]
tuple_of_integers = tuple(input_list)

print(f"input tuple elements: {tuple_of_integers}")
print(f"Mean of elements in the tuple: {tuple_mean(tuple_of_integers)}")
    
"""
	------- output 1 --------
    Enter a tuple of integers separated by spaces: 1 2 3 4 5
    input tuple elements: (1, 2, 3, 4, 5)
    Mean of elements in the tuple: 3.0

	------- output 2 --------
    Enter a tuple of integers separated by spaces: 2 5 7 10 11
    input tuple elements: (2, 5, 7, 10, 11)
    Mean of elements in the tuple: 7.0
"""