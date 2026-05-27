from shape import Shape

class Rectangle(Shape):
    """
    Updating the constant variables
    and adding height and width parameters
    """
    def __init__(self, height, wight):
        super().__init__(shape_type="rectangle")
        self.height = height
        self.wight = wight

    def get_area(self):
        """
        Returns the area of a rectangle
b       by calculating height times width
        """
        return self.height * self.wight

    def get_perimeter(self):
        """
        Returns the perimeter of a rectangle
        by calculating twice the height + twice the width
        """
        return self.height * 2 + self.wight * 2

    def to_dict(self):
        """
        A function that adds the results to a ready dictionary
        for future insertion into the json file
        """
        return self.__dict__


def main():
    if __name__ == "__main__":
        b1 = Rectangle(4, 2)
        b1.get_area()
        b1.get_perimeter()
        print(b1.to_dict())

main()