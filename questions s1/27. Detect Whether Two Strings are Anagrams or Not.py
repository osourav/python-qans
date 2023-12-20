"""
	Write a program to detect whether two strings are anagrams or not. 
"""

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1.lower(), string2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    
"""
	------- output --------
    Enter the first string: Listen
    Enter the second string: Silent
    The strings are anagrams.
"""