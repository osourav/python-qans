"""
	Write a program to copy the first 100 characters of a binary file into another. 
"""

input_file = input("Enter the input binary file name: ")
output_file = input("Enter the output binary file name: ")

try:
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        data = infile.read(100)
        outfile.write(data)
        infile.close()
        outfile.close()
        print("Copy the first 100 characters Successfully")

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    
"""
	------- output --------
    Enter the input binary file name: my_file.txt     
    Enter the output binary file name: output_file.txt
    Copy the first 100 characters Successfully

    ------- output_file.txt contains -------
    Hello!
    this is a demo file
    i am 22 years old
    and my hobby is programming
    Thank you for visit
    se
"""