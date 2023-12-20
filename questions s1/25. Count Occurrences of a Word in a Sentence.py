"""
	Write a program to count the occurrences of a word in a given sentence. 
"""

sentence = input("Enter a sentence: ")
word_to_count = input("Enter the word to count: ")

word_count = sentence.lower().split().count(word_to_count.lower())
print(f"Occurrences of '{word_to_count}' in the sentence: {word_count}")
    
"""
	------- output --------
    Enter a sentence: hello hi welcome hi      
    Enter the word to count: hi
    Occurrences of 'hi' in the sentence: 2

"""