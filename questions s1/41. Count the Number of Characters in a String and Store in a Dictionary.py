"""
	Write a program to count the numbers of characters in a string and store them in a dictionary. 
"""

input_string = input("Enter a string: ")

char_count = {char: input_string.count(char) for char in set(input_string)}
print("Character counts:", char_count)

"""
	------- output 1 --------
    Enter a string: hello
    Character counts: {'e': 1, 'l': 2, 'h': 1, 'o': 1}

	------- output 2 --------
    Enter a string: welcome
    Character counts: {'m': 1, 'o': 1, 'w': 1, 'e': 2, 'c': 1, 'l': 1}
"""