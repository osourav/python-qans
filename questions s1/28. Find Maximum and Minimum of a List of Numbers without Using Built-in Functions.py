"""
	Write a program to find the maximum and minimum of a list of numbers without using built-in functions. 
"""

inp = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in inp.split()]

if len(numbers) > 0:
    max_num = min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    print(f"Maximum number: {max_num}, Minimum number: {min_num}")
else:
    print("List is empty.")
    
"""
	------- output --------
    Enter numbers separated by spaces: 10 20 15 60 44 5 100
    Maximum number: 100, Minimum number: 5
"""