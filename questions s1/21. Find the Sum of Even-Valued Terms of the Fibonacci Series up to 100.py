"""
	Write a program to find the sum of the even-valued terms of the Fibonacci series up to 100. 
"""

fibonacci_series = [0, 1]
even_sum = 0

while True:
    next_term = fibonacci_series[-1] + fibonacci_series[-2]
    if next_term > 100:
        break
    fibonacci_series.append(next_term)

for term in fibonacci_series:
    if term % 2 == 0:
        even_sum += term

print(f"Sum of even-valued terms in the Fibonacci series up to 100: {even_sum}")

"""
	------- output --------
    Sum of even-valued terms in the Fibonacci series up to 100: 44

"""