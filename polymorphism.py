"""
Polymorphism
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):

    def __init__(self, topping: str, radius: float):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(5), Square(10), Triangle(5, 10), Pizza("cheese", 5)]

for shape in shapes:
    print(shape.area())
