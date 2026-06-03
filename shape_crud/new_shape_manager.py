import json
from json import JSONDecodeError
from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.shapes = self.load_from_json()
        self._update_next_id()

    def _update_next_id(self):
        if self.shapes:
            self.next_id = max(s.shape_id for s in self.shapes) + 1
        else:
            self.next_id = 1

    def create_shape(self, data):
        shape_type = data.get("shape_type")

        if shape_type == "square":
            my_shape = Square(side=data.get("side"), shape_id=self.next_id)
        elif shape_type == "rectangle":
            my_shape = Rectangle(height=data.get("height"), width=data.get("width"), shape_id=self.next_id)
        elif shape_type == "circle":
            my_shape = Circle(radius=data.get("radius"), shape_id=self.next_id)
        else:
            raise TypeError("Invalid shape type")

        self.shapes.append(my_shape)
        self.save_to_json(self.shapes)
        self._update_next_id()
        return my_shape

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, **kwargs):
        shape = self.find_id(shape_id)
        if shape:
            for key, value in kwargs.items():
                if hasattr(shape, key):
                    setattr(shape, key, value)
            self.save_to_json(self.shapes)
            return shape
        return None

    def delete_shape(self, shape_id):
        shape = self.find_id(shape_id)
        if shape:
            self.shapes.remove(shape)
            self.save_to_json(self.shapes)
            return True
        return False

    def save_to_json(self, data):
        serialized_data = []
        for shape in data:
            if hasattr(shape, "to_dict"):
                serialized_data.append(shape.to_dict())
            else:
                serialized_data.append(shape)

        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(serialized_data, file, ensure_ascii=False, indent=4)

    def load_from_json(self):
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                objects_list = []
                for item in data:
                    if item["shape_type"] == "square":
                        my_object = Square(side=item["side"], shape_id=item["shape_id"])
                    elif item["shape_type"] == "rectangle":
                        my_object = Rectangle(height=item["height"], width=item["width"], shape_id=item["shape_id"])
                    elif item["shape_type"] == "circle":
                        my_object = Circle(radius=item["radius"], shape_id=item["shape_id"])
                    else:
                        continue
                    objects_list.append(my_object)
                return objects_list
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def find_id(self, shape_id):
        for i in self.shapes:
            if i.shape_id == int(shape_id):
                return i
        return None

    def get_total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()
        return total