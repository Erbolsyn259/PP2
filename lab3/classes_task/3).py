class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,lengh,width):
        self.lengh = lengh
        self.width = width
    def area(self):
        return self.lengh * self.width

rectangle = Rectangle(4,5)

print(rectangle.area())
        