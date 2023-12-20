"""
	Create a module to check if a passed string is a palindrome or not. Write a program to find whether a string is a palindrome or not using this module. 
"""

from palindrome_module import is_palindrome

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
"""
	------- output 1 --------
    Enter a string: lol
    The string is a palindrome.

	------- output 2 --------
    Enter a string: 123  
    The string is not a palindrome.
"""