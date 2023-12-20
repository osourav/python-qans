"""
   Write a program to convert temperature from degree Celsius to degree Fahrenheit
"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

"""
   ------- output 1 --------
   Enter temperature in Celsius: 0
   0.0 degrees Celsius is equal to 32.0 degrees Fahrenheit.

   ------- output 2 --------
   Enter temperature in Celsius: 45
   45.0 degrees Celsius is equal to 113.0 degrees Fahrenheit.
"""
