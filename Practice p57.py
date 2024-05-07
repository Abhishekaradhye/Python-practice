# Write a  Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.

import math 

class shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return "{:.2f}".format(math.pi * self.radius**2)
    def calculate_perimeter(self):
        return "{:.2f}".format(2 * math.pi * self.radius)
    
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    def calculate_area(self):
        return "{:.2f}".format(self.length * self.width)
    def calculate_perimeter(self):
        return "{:.2f}".format(2 * (self.length + self.width))
    
class triangle(shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        return "{:.2f}".format(0.5 * self.base * self.height)
    def calculate_perimeter(self):
        return "{:.2f}".format(self.side1 + self.side2 + self.side3)
    
my_circle = circle(8)
circle_area = my_circle.calculate_area()
circle_circumference = my_circle.calculate_perimeter()

print(f"Area of circle :{circle_area} sq.mm")
print(f"Circumference of circle :{circle_circumference} mm")

my_triangle = triangle(4, 5, 3, 4, 6)
print("\nTriangle:")
print("Area:", my_triangle.calculate_area())
print("Perimeter:", my_triangle.calculate_perimeter())

my_rectangle = rectangle(10, 8)
print("\nSquare:")
print("Area:", my_rectangle.calculate_area())
print("Perimeter:", my_rectangle.calculate_perimeter())
        
        



