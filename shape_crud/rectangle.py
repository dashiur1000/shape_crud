from shape import Shape

class Rectangle(Shape):
    def __init__(self, height, weight, shape_id, shape_type):
        super().__init__(shape_id=2, shape_type="rectangle")
        self.height = height
        self.weight = weight

    def get_area(self):
        return self.height * self.weight

    def get_perimeter(self):
        return self.height * 2 + self.weight * 2