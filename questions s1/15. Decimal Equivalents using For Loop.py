"""
	Write a program to print the decimal equivalents of 1/2, 1/3, 1/4,..., 1/10 using a for loop. 
"""

for i in range(2, 11):
    decimal_equivalent = 1 / i
    print(f"Decimal equivalent of 1/{i} is {decimal_equivalent}")

"""
	------- output --------
    Decimal equivalent of 1/2 is 0.5
    Decimal equivalent of 1/3 is 0.3333333333333333
    Decimal equivalent of 1/4 is 0.25
    Decimal equivalent of 1/5 is 0.2
    Decimal equivalent of 1/6 is 0.16666666666666666
    Decimal equivalent of 1/7 is 0.14285714285714285
    Decimal equivalent of 1/8 is 0.125
    Decimal equivalent of 1/9 is 0.1111111111111111
    Decimal equivalent of 1/10 is 0.1
"""
