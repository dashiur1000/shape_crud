import json

import shape
from square import Square
from circle import Circle
from  rectangle import Rectangle

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape_type, **kwargs):
        if shape_type == 1:
            my_shape = Square(side=kwargs["side"])
            my_shape.to_dict()
        elif shape_type == 2:
            my_shape = Rectangle(height=kwargs["height"], weight=kwargs["weight"])
            my_shape.to_dict()
        elif shape_type == 3:
            my_shape = Circle(radius=kwargs["radius"])
            my_shape.to_dict()



    def get_all_shapes(self):
        pass

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        pass

    def save_to_json(self, data):
        with open("shapes.json", "a", encoding="utf-8") as file:
            json.dump(self.data, file)


    def load_from_json(self, data):
        with open("shapes.json", "r+", encoding="utf-8") as file:
            self.data = json.load(file)
            return data

