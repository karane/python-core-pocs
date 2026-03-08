from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        """Name of the shape"""
        pass

    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass

    @classmethod
    @abstractmethod
    def shape_type(cls):
        """Return type of the shape (e.g., '2D', '3D')"""
        pass

    @staticmethod
    @abstractmethod
    def description():
        """Return a static description of shapes"""
        pass


# Concrete subclass implementing all abstract members
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def name(self):
        return "Circle"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    @classmethod
    def shape_type(cls):
        return "2D"

    @staticmethod
    def description():
        return "A shape with all points equidistant from its center."


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def name(self):
        return "Square"

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    @classmethod
    def shape_type(cls):
        return "2D"

    @staticmethod
    def description():
        return "A shape with four equal sides and four right angles."


if __name__ == "__main__":
    shapes = [Circle(3), Square(4)]

    for shape in shapes:
        print(f"Shape: {shape.name}")
        print(f" - Type: {shape.shape_type()}")
        print(f" - Area: {shape.area():.2f}")
        print(f" - Perimeter: {shape.perimeter():.2f}")
        print(f" - Description: {shape.description()}")
        print()
