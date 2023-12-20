"""
	Write a program to define a function that accepts a string and calculates the number of uppercase letters and lowercase letters. 
"""

def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = input("Enter a string: ")
uppercase_count, lowercase_count = count_upper_lower(input_string)

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
    
"""
	------- output 1 --------
    Enter a string: Hello World
    Uppercase letters: 2
    Lowercase letters: 8

	------- output 2 --------
    Enter a string: Welcome
    Uppercase letters: 1
    Lowercase letters: 6
"""