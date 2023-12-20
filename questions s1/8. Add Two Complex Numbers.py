"""
	Write a program to add two complex numbers by reading the numbers from the user. 
"""

real_part1 = float(input("Enter the real part of the first complex number: "))
imag_part1 = float(input("Enter the imaginary part of the first complex number: "))
real_part2 = float(input("Enter the real part of the second complex number: "))
imag_part2 = float(input("Enter the imaginary part of the second complex number: "))
complex1 = complex(real_part1, imag_part1)
complex2 = complex(real_part2, imag_part2)
sum_complex = complex1 + complex2
print("Sum of complex numbers:", sum_complex)
    
"""
	------- output 1 --------
    Enter the real part of the first complex number: 4
    Enter the imaginary part of the first complex number: 3
    Enter the real part of the second complex number: 5
    Enter the imaginary part of the second complex number: 2
    Sum of complex numbers: (9+5j)

	------- output 2 --------
    Enter the real part of the first complex number: 10
    Enter the imaginary part of the first complex number: 5
    Enter the real part of the second complex number: 20
    Enter the imaginary part of the second complex number: 3
    Sum of complex numbers: (30+8j)
"""