"""
	Write a program to read a string and check whether the string is a palindrome or not. 
"""

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")
    
"""
	------- output 1 --------
    Enter a string: lol
    lol is a palindrome

	------- output 2 --------
    Enter a string: hello
    hello is not a palindrome
"""