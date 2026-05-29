import json
from json import JSONDecodeError

from square import Square
from circle import Circle
from rectangle import Rectangle

class ShapeManager:
    """
    Functions for handling shapes
    and menu helper functions
    """
    def __init__(self):
        self.shapes = self.load_from_json()
        self._update_next_id()


    def _update_next_id(self):
        """
        Setting the ID number according to the number of shapes
        """
        if self.shapes:
            self.next_id = max(s.shape_id for s in self.shapes) + 1
        else:
            self.next_id = 1

    def create_shape(self, shape_type, **kwargs):
        """
        Creating a shape with its special parameters
        """
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
        """
        View existing shapes
        """
        data = []
        try:
            shapes_list = self.load_from_json()
            if not shapes_list:
                print("==================\nthe file is empty\n==================\n")
            for form in shapes_list:
                self.print_shapes(form)

        except (TypeError, JSONDecodeError):
            with open("shapes.json", "w", encoding="utf-8") as f:
                f.write("[]")


    def update_shape(self, shape_id, **kwargs):
        """
        Updating the size of shapes
        """
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
        """
        Delete a shape if it exists
        """
        shape = self.find_id(shape_id)
        if shape:
            self.shapes.remove(shape)
            self.save_to_json(self.shapes)
            print("delete this shape!")
        else:
            print("not found!")

    def save_to_json(self, data):
        """
        Saves the shapes to the json file
        """
        lst = [s.to_dict() for s in data]
        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(lst, file)


    def load_from_json(self):
        """
        Loading the shapes from the json file
        """
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
        """
        Prints the existing shapes in the configuration.
        """
        print(f"id: {shape_object.shape_id}")
        print(f"type: {shape_object.shape_type}")

        if shape_object.shape_type == "square":
            print(f"side: {shape_object.side}")
        elif shape_object.shape_type == "circle":
            print(f"radius: {shape_object.radius}")
        elif shape_object.shape_type == "rectangle":
            print(f"width: {shape_object.width}, height: {shape_object.height}")

        print(f"area: {round(shape_object.get_area(), 4)}")
        print(f"perimeter: {round(shape_object.get_perimeter(), 4)}")
        print("======================")


    def find_id(self, shape_id):
        """
        Search for existing or non-existing shapes
        """
        for i in self.shapes:
            if i.shape_id == int(shape_id):
                return i
        return False