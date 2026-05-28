from shape import Shape

class Square(Shape):
    """
    Updating the constant variables
    and adding a parameter of the side
    """
    def __init__(self, side, shape_id):
        super().__init__(shape_type="square", shape_id=shape_id)
        self.side = side

    def get_area(self):
        """
        Returns the area of a quadrilateral
        by calculating side times side
        """
        return self.side * self.side

    def get_perimeter(self):
        """
        Returns the perimeter of a square
        by calculating the side times 4
        """
        return self.side * 4

    def to_dict(self):
        """
        A function that adds the results to a ready dictionary
        for future insertion into the json file
        """
        return self.__dict__

def main():
    a1 = Square(5, 18)
    a1.get_area()
    a1.get_perimeter()
    print(a1.to_dict())

if __name__ == "__main__":
    main()

