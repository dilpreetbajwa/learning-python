"""
Property
"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"

    @width.setter
    def width(self, value: int):
        if value < 0:
            raise ValueError("Width must be positive")

        self._width = value

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"

    @height.setter
    def height(self, value: int):
        if value < 0:
            raise ValueError("Height must be positive")

        self._height = value


rectangle = Rectangle(10, 20)

print(rectangle.width)
print(rectangle.height)
