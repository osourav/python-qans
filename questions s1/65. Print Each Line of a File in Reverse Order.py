"""
	Write a program to print each line of a file in reverse order. 
"""

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())
        file.close()

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    
"""
	------- output 1 --------
    --- bye bye ---
    see you soon
    Thank you for visit
    and my hobby is programming
    i am 22 years old
    this is a demo file
    Hello!

	------- output 2 --------
    Enter the file name: my_txt
    Error: File 'my_txt' not found.
"""