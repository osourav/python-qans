"""
	Write a program to get all substrings of a given string. 
"""

input_string = input("Enter a string: ")
substrings = set([])

for i in range(len(input_string)):
   for j in range(i + 1, len(input_string) + 1):
      substrings.add(input_string[i:j])

print("All substrings:", substrings)
    
"""
	------- output 1 --------
    Enter a string: hello
    All substrings: {'hell', 'ell', 'ello', 'hello', 'el', 'h', 'llo', 'he', 'lo', 'll', 'o', 'hel', 'l', 'e'}

	------- output 2 --------
    Enter a string: abc
    All substrings: {'b', 'abc', 'a', 'ab', 'c', 'bc'}
"""