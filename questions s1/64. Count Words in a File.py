"""
	Write a program to accept a filename from the user and count the number of words present in the file. 
"""

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        print(f"Number of words in the file: {word_count}")
        file.close()

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")

"""
	------- output 1 --------
    Enter the file name: my_file.txt
    Number of words in the file: 20

	------- output 2 --------
    Enter the file name: my.txt
    Error: File 'my.txt' not found.
"""