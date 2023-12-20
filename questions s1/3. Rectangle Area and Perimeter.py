"""
   Write a program to calculate the area and perimeter of a rectangle.
"""

length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")


"""
   ------- output 1 --------
   Enter length of the rectangle: 10
   Enter width of the rectangle: 12
   Area of the rectangle: 120.0    
   Perimeter of the rectangle: 44.0

   ------- output 2 --------
   Enter length of the rectangle: 20
   Enter width of the rectangle: 10
   Area of the rectangle: 200.0    
   Perimeter of the rectangle: 60.0
"""
