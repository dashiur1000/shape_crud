from shape import Shape

class Square(Shape):
    """
    Updating the constant variables
    and adding a parameter of the side
    """
    def __init__(self, side, shape_id, shape_type):
        super().__init__(shape_id=1, shape_type="square")
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
        pass