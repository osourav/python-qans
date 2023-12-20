"""
	Write a program using a while loop to print all the odd numbers within a given range. 
"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

current_number = start
print("Odd numbers:", end=" ")
while current_number <= end:
    if current_number % 2 != 0:
        print(current_number, end=" ")
    current_number += 1
print()
    
"""
	------- output 1 --------
    Enter the starting number: 1
    Enter the ending number: 20
    Odd numbers: 1 3 5 7 9 11 13 15 17 19 

	------- output 2 --------
    Enter the starting number: 5
    Enter the ending number: 25
    Odd numbers: 5 7 9 11 13 15 17 19 21 23 25 
"""