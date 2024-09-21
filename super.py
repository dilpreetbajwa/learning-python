"""
Super
"""


class Shape:
    def __init__(self, color: str, is_filled: bool):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color: str, is_filled: bool, radius: float):
        super().__init__(color, is_filled)
        self.radius = radius

    # Overriding the describe method
    def describe(self):
        print(f"It is a circle with an are of {3.14 * self.radius ** 2}cm²")
        super().describe()


class Square(Shape):
    def __init__(self, color: str, is_filled: bool, width: float):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width ** 2}cm²")
        super().describe()


class Triangle(Shape):
    def __init__(self, color: str, is_filled: bool, width: float, height: float):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}cm²")
        super().describe()


circle = Circle("red", True, 5)
square = Square("blue", False, 10)
triangle = Triangle("green", True, 5, 10)

print(circle.color)
print(circle.is_filled)
print(f"Circle radius: {circle.radius}cm")

circle.describe()
square.describe()
triangle.describe()
