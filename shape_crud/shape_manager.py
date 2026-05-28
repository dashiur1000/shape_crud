import json
from json import JSONDecodeError

import shape
from square import Square
from circle import Circle
from rectangle import Rectangle

class ShapeManager:
    def __init__(self):
        self.shapes = self.load_from_json()
        self._update_next_id()

        if self.shapes:
            self.next_id = max(shape.shape_id for shape in self.shapes) + 1


    def _update_next_id(self):
        if self.shapes:
            self.next_id = max(s.shape_id for s in self.shapes) + 1
        else:
            self.next_id = 1

    def create_shape(self, shape_type, **kwargs):
        current_id = self.next_id

        if shape_type == 1:
            my_shape = Square(side=kwargs["side"], shape_id=self.next_id)
        elif shape_type == 2:
            my_shape = Rectangle(height=kwargs["height"], width=kwargs["width"], shape_id=self.next_id)
        elif shape_type == 3:
            my_shape = Circle(radius=kwargs["radius"], shape_id=self.next_id)
        else:
            raise TypeError("Error! dont have shape type")

        my_shape.shape_id = self.next_id
        self.shapes.append(my_shape)
        self.save_to_json(self.shapes)
        self.next_id += 1


    def get_all_shapes(self):
        data = []
        try:
            shapes_list = self.load_from_json()
            if not shapes_list:
                print("the file is empty")
            for form in shapes_list:
                self.print_shapes(form)

        except (TypeError, JSONDecodeError):
            with open("shapes.json", "w", encoding="utf-8") as f:
                f.write("[]")

    def update_shape(self, shape_id, **kwargs):
        shape = self.find_id(shape_id)
        if shape:
            for key, value in kwargs.items():
                if  key == "side":
                    shape.side = value
                elif key == "radius":
                    shape.radius = value
                elif key == "width":
                    shape.width = value
                elif key == "height":
                    shape.height = value
            self.save_to_json(self.shapes)



    def delete_shape(self, shape_id):
        shape = self.find_id(shape_id)
        if shape:
            self.shapes.remove(shape)
            self.save_to_json(self.shapes)
            print("delete this shape!")
        else:
            print("not found!")

    def save_to_json(self, data):
        lst = [s.to_dict() for s in data]
        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(lst, file)


    def load_from_json(self):
        try:
            with open("shapes.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                objects_list = []
                for item in data:
                    if item["shape_type"] == "square":
                        my_object = Square(side=item["side"], shape_id=item["shape_id"])
                    elif item["shape_type"] == "rectangle":
                        my_object = Rectangle(height=item["height"], width=item["width"], shape_id=item["shape_id"])
                    elif item["shape_type"] == "circle":
                        my_object = Circle(radius=item["radius"], shape_id=item["shape_id"])
                    objects_list.append(my_object)
                return objects_list
        except (json.JSONDecodeError, FileNotFoundError):
            with open("shapes.json", "w", encoding="utf-8") as f:
                f.write("[]")
                return []


    def print_shapes(self, shape_object):
        print(f"id: {shape_object.shape_id}, type: {shape_object.shape_type}")


    def find_id(self, shape_id):
        for i in self.shapes:
            if i.shape_id == int(shape_id):
                return i
        return False