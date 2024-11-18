#!/usr/bin/python3
class Rectangle:
    def __init__(self, length, width):
        """initialize instance variables for length and width"""
        self.length = length
        self.width = width

    @property
    def area(self):
        """calculate area of the rectangle"""
        return self.length * self.width
    
    @property
    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        return 2 * (self.length + self.width)
    
    def __str__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle(Length: {self.length}, Width: {self.width})"
    
    def __eq__(self, other):
        """compare two rectangles based on their areas"""
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented
    
if __name__ == "__main__":
    """create two instances with different dimensions"""
    rectangle1 = Rectangle(4, 6)
    rectangle2 = Rectangle(5, 7)
    """print details of rectangle"""
    print(rectangle1)
    print(rectangle2)

    """print area and perimeter of rectangle1"""
    print(f"Area of rectangle1: {rectangle1.area}")
    print(f"Perimeter of rectangle1: {rectangle1.perimeter}")

    """print area and perimeter of rectangle2"""
    print(f"Area of rectangle2: {rectangle2.area}")
    print(f"Perimeter of rectangle2: {rectangle2.perimeter}")

    """compare the two rectangles"""
    print(f"Are the areas of rectangle1 and rectangle2 equal? {rectangle1 == rectangle2}")