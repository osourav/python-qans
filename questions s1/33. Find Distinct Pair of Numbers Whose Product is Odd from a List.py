"""
	Write a program to find the distinct pair of numbers whose product is odd from a list of integers. 
"""

inp = input("Enter the list of numbers separated by spaces: ")
numbers = [int(x) for x in inp.split()]
distinct_pairs = []

for i, num1 in enumerate(numbers):
    for num2 in numbers[i + 1 :]:
        if (num1 * num2) % 2 == 1:
            distinct_pairs.append((num1, num2))

print("Distinct pairs whose product is odd:", distinct_pairs)

"""
	------- output 1 --------
    Enter the list of numbers separated by spaces: 1 2 3 4 5 6 7 8
    Distinct pairs whose product is odd: [(1, 3), (1, 5), (1, 7), (3, 5), (3, 7), (5, 7)]

	------- output 2 --------
    Enter the list of numbers separated by spaces: 4 5 6 7 8 9 
    Distinct pairs whose product is odd: [(5, 7), (5, 9), (7, 9)]
"""
