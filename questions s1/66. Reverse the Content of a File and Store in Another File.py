"""
	Write a program to reverse the content of a file and store it in another file. 
"""


input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        reversed_content = content[::-1]
        outfile.write(reversed_content)
        infile.close()
        outfile.close()
        print("Stored content successfully")

except FileNotFoundError:
    print(f"Error: One or both files not found.")
    
"""
	------- output --------
    Enter the input file name: my_file.txt
    Enter the output file name: output_file.txt
    Stored content successfully

	------- output_file.txt contains -------
    --- eyb eyb ---
    noos uoy ees
    tisiv rof uoy knahT
    gnimmargorp si ybboh ym dna
    dlo sraey 22 ma i
    elif omed a si siht
    !olleH
"""