# Parent class
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


rect = Rectangle(10, 5)
sq = Square(4)

print("Area of Rectangle:", rect.area())
print("Area of Square:", sq.area())
