"""
	Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triangle from Polygon and write methods to get the details of their dimensions and hence calculate the area. 
"""

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_dimensions(self):
        return f"Length: {self.length}, Width: {self.width}"

    def calculate_area(self):
        return self.length * self.width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_dimensions(self):
        return f"Base: {self.base}, Height: {self.height}"

    def calculate_area(self):
        return 0.5 * self.base * self.height

rectangle = Rectangle(5, 8)
print("Rectangle Details:", rectangle.get_dimensions())
print("Rectangle Area:", rectangle.calculate_area())

triangle = Triangle(4, 6)
print("\nTriangle Details:", triangle.get_dimensions())
print("Triangle Area:", triangle.calculate_area())

    
"""
	------- output -------
    Rectangle Details: Length: 5, Width: 8
    Rectangle Area: 40

    Triangle Details: Base: 4, Height: 6
    Triangle Area: 12.0
"""