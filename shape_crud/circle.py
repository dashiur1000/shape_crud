from shape import Shape
from math import pi

class Circle(Shape):
    """
    Updating the constant variables
    and adding height and width parameters
    """
    def __init__(self, radius):
        super().__init__(shape_type="circle")
        self.radius = radius

    def get_area(self):
        """
        Returns the area of a circle
b       by radius squared times pi
        """
        return (self.radius**2) * pi

    def get_perimeter(self):
        """
        Returns the perimeter of a circle
        by radius times 2 py
        """
        return self.radius * 2 * pi

    def to_dict(self):
        """
        A function that adds the results to a ready dictionary
        for future insertion into the json file
        """
        return self.__dict__


def main():
    if __name__ == "__main__":
        b1 = Circle(4)
        b1.get_area()
        b1.get_perimeter()
        print(b1.to_dict())

main()