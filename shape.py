from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    try:
        rectangle = Rectangle(5, 10)
        print(f"Площадь прямоугольника (5x10): {rectangle.area():.2f}")

        circle = Circle(7)
        print(f"Площадь круга (радиус=7): {circle.area():.2f}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
