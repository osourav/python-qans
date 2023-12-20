"""
	Write a program to count the number of each vowel in a sentence. 
"""

sentence = input("Enter a sentence: ")
vowel_count = { "a": 0, "e": 0, "i": 0, "o": 0, "u": 0 }

for char in sentence:
    char_lower = char.lower()
    if char_lower in vowel_count:
        vowel_count[char_lower] += 1

print("Vowel counts:", vowel_count)

"""
	------- output 1 --------
    Enter a sentence: Hello World 
    Vowel counts: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}

	------- output 2 --------
    Enter a sentence: Audio
    Vowel counts: {'a': 1, 'e': 0, 'i': 1, 'o': 1, 'u': 1}
"""
