"""
	Write a program to find all the numbers divisible by 5 and 7 between the given range using the lambda function. 
"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


result = list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end + 1)))
print("Numbers divisible by 5 and 7:", result)
    
"""
	------- output 1 --------
    Enter the starting number: 1 
    Enter the ending number: 100
    Numbers divisible by 5 and 7: [35, 70]

	------- output 2 --------
    Enter the starting number: 20
    Enter the ending number: 200
    Numbers divisible by 5 and 7: [35, 70, 105, 140, 175]
"""