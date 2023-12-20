"""
	Write a program that prompts users to enter numbers. This process repeats until the user enters -1. Finally, the program prints the count of prime and composite numbers entered. 
"""

def is_prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    return False

prime_count = 0
composite_count = 0

while True:
    num = int(input("Enter a number (or -1 to exit): "))
    if num == -1:
        break

    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1

print(f"Count of prime numbers: {prime_count}")
print(f"Count of composite numbers: {composite_count}")
    
"""
	------- output --------
    Enter a number (or -1 to exit): 10
    Enter a number (or -1 to exit): 7
    Enter a number (or -1 to exit): 5
    Enter a number (or -1 to exit): -1
    Count of prime numbers: 2
    Count of composite numbers: 1
"""