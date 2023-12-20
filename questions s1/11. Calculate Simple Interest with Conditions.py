"""
	Write a program to calculate simple interest with the following conditions: If the principal amount is less than 2,00,000, the interest rate is 10%. If the principal amount is 2,00,000 - 10,00,000, the interest rate is 12%. If the principal amount is greater than 10,00,000, the interest rate is 15%. 
"""

principal_amount = float(input("Enter the principal amount: "))

if principal_amount < 2_00_000:
    interest_rate = 10
elif 2_00_000 <= principal_amount <= 10_00_000:
    interest_rate = 12
else:
    interest_rate = 15

duration = float(input("Enter the duration (in years): "))
interest_amount = (principal_amount * interest_rate * duration) / 100
total_amount = principal_amount + interest_amount

print(f"Interest Amount: {interest_amount}, Total Amount: {total_amount}")
    
"""
	------- output 1 --------
    Enter the principal amount: 50000 
    Enter the duration (in years): 5
    Interest Amount: 25000.0, Total Amount: 75000.0

	------- output 2 --------
    Enter the principal amount: 250000
    Enter the duration (in years): 3
    Interest Amount: 90000.0, Total Amount: 340000.0
    
	------- output 3 --------
    Enter the principal amount: 3000000
    Enter the duration (in years): 12
    Interest Amount: 5400000.0, Total Amount: 8400000.0
"""