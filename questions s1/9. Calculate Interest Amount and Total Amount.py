"""
	Write a program to accept the principal amount, rate of interest, and duration from the user. Calculate the interest amount and the total amount (principal + interest). 
"""

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
duration = float(input("Enter the duration (in years): "))
interest_amount = (principal_amount * rate_of_interest * duration) / 100
total_amount = principal_amount + interest_amount
print(f"Interest Amount: {interest_amount}, Total Amount: {total_amount}")
    
"""
	------- output 1 --------
    Enter the principal amount: 5500
    Enter the rate of interest: 2
    Enter the duration (in years): 3
    Interest Amount: 330.0, Total Amount: 5830.0

	------- output 2 --------
    Enter the rate of interest: 4
    Enter the duration (in years): 5
    Interest Amount: 5000.0, Total Amount: 30000.0
"""