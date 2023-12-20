"""
	Write a program to find the sum of all prime numbers within a given range. 
"""

def is_prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    return False

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
prime_sum = 0

for num in range(start, end + 1):
    if is_prime(num):
        prime_sum += num

print(f"Sum of prime numbers between {start} and {end} is {prime_sum}")
    
"""
	------- output 1 --------
    Enter the starting number: 3
    Enter the ending number: 100
    Sum of prime numbers between 3 and 100 is 1058

	------- output 2 --------
    Enter the starting number: 1
    Enter the ending number: 10
    Sum of prime numbers between 1 and 10 is 17
"""