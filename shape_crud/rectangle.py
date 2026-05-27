from shape import Shape

class Rectangle(Shape):
    """
    Updating the constant variables
    and adding height and width parameters
    """
    def __init__(self, height, weight, shape_id, shape_type):
        super().__init__(shape_id=2, shape_type="rectangle")
        self.height = height
        self.weight = weight

    def get_area(self):
        """
        Returns the area of a rectangle
b       by calculating height times width
        """
        return self.height * self.weight

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        by calculating twice the height + twice the width
        """
        return self.height * 2 + self.weight * 2

    def to_dict(self):
        """
        A function that adds the results to a ready dictionary
        for future insertion into the json file
        """
        pass