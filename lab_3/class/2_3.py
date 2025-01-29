class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Площадь фигуры Shape:", shape.area())
a = int(input("Введите длину стороны квадрата: "))
square = Square(a)
print("Площадь квадрата:", square.area())


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

b = int(input("Введите длину прямоугольника: "))
c = int(input("Введите ширину прямоугольника: "))
rect = Rectangle(b, c)
print("Площадь прямоугольника:", rect.area())

