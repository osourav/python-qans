"""
	Write a program to copy the content of the text file to another file by converting all lowercase characters to uppercase. 
"""


input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        uppercase_content = content.upper()
        outfile.write(uppercase_content)
        infile.close()
        outfile.close()
        print("Uppercase characters copy successfully")

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    
"""
	------- output --------
    Enter the input file name: my_file.txt     
    Enter the output file name: output_file.txt
    Uppercase characters copy successfully

    ------- output_file.txt contains -------
    HELLO!
    THIS IS A DEMO FILE
    I AM 22 YEARS OLD
    AND MY HOBBY IS PROGRAMMING
    THANK YOU FOR VISIT
    SEE YOU SOON
    --- BYE BYE ---
"""