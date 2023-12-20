"""
	Write a program to check whether a given number is an Armstrong number or not. 
"""

num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
    
"""
	------- output 1 --------
    Enter a number: 153
    153 is an Armstrong number

	------- output 2 --------
    Enter a number: 123
    123 is not an Armstrong number
"""