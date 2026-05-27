from shape import Shape

class Square(Shape):
    def __init__(self, rid, shape_id, shape_type):
        super().__init__(shape_id=1, shape_type="square")
        self.rid = rid

    def get_area(self):
        return self.rid * self.rid

    def get_perimeter(self):
        return self.rid * 4