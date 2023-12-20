"""
	Write a program to copy one Python script into another in such a way that all comment lines are skipped and not copied to the destination file. 
"""


input_file = input("Enter the input Python script file name: ")
output_file = input("Enter the output Python script file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip().startswith('#'):
                outfile.write(line)
        infile.close()
        outfile.close()
        print(f"Successfully copied script, excluding comments, from '{input_file}' to '{output_file}'.")


except FileNotFoundError:
    print(f"Error: One or both files not found.")

"""
    ------- hello_world.py contains -------
    #this is a simple hello world program
    print("Hello World!")
    
	------- output -------
    Enter the input Python script file name: hello_world.py
    Enter the output Python script file name: my.py
    Successfully copied script, excluding comments, from 'hello_world.py' to 'my.py'.

	------- my.py contains -------
    print("Hello World!") 
"""