class Shape:
    """
    Saving variables for update
    """
    _counter = 0

    def __init__(self, shape_type, shape_id):
        Shape._counter += 1
        self.shape_id = shape_id
        self.shape_type = shape_type

    def get_area(self):
        """
        Area measurement function
        """
        pass

    def get_perimeter(self):
        """
        Area measurement function
        """
        pass

    def to_dict(self):
        """
        A function that adds the results to a ready dictionary
        for future insertion into the json file
        """
        pass