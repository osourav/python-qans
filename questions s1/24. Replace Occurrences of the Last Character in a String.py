"""
	Write a program to get a string from a given string where all occurrences of the last character have been changed to '*' except the last character. 
"""

input_string = input("Enter a string: ")

if len(input_string) > 0:
    last_char = input_string[-1]
    modified_string = input_string[:-1] + '*'
    print(f"Modified string: {modified_string}")
else:
    print("String is empty.")
    
"""
	------- output --------
    Enter a string: hello
    Modified string: hell*

"""