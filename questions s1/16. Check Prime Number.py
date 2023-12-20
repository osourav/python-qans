"""
	Write a program to check whether a given number is a prime number or not. 
"""

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
"""
	------- output 1 --------
    Enter a number: 11
    11 is a prime number

	------- output 2 --------
    Enter a number: 9
    9 is not a prime number
"""