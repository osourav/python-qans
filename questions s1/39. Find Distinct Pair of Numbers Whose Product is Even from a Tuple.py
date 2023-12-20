"""
	Write a program to find the distinct pair of numbers whose product is even from a tuple of integers. 
"""

inp = input("Enter a tuple of integers separated by spaces: ")
tuple_of_integers = tuple([int(x) for x in inp.split()])
distinct_pairs = []

for i, num1 in enumerate(tuple_of_integers):
    for num2 in tuple_of_integers[i + 1 :]:
        if (num1 * num2) % 2 == 1:
            distinct_pairs.append((num1, num2))

print("input tuple:", tuple_of_integers)
print("Distinct pairs whose product is even:", distinct_pairs)
    
"""
	------- output 1 --------
    Enter a tuple of integers separated by spaces: 1 2 3 4 5 6 7
    input tuple: (1, 2, 3, 4, 5, 6, 7)
    Distinct pairs whose product is even: [(1, 3), (1, 5), (1, 7), (3, 5), (3, 7), (5, 7)]

	------- output 2 --------
    Enter a tuple of integers separated by spaces: 5 10 15 20 25
    input tuple: (5, 10, 15, 20, 25)
    Distinct pairs whose product is even: [(5, 15), (5, 25), (15, 25)]
"""