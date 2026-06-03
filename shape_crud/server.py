import uvicorn

from new_shape_manager import ShapeManager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
manager = ShapeManager()


class ShapeInit(BaseModel):
    shape_type: str
    side: float
    radius: float
    height: float
    width: float


@app.get("/shapes/total-area")
def all_shapes_area():
    """
    Summarize the total area of all existing shapes
    :return:
    area
    """
    area = manager.get_total_area()
    return area


@app.get("/shapes/{id}")
def return_shape(id: int):
    """
    Displays a certain shape
    :param id:
    :return: shape
    """
    find = manager.find_id(id)
    if find is None:
        raise HTTPException(status_code=404, detail="not found")
    return find.to_dict()


@app.put("/shapes/{id}")
def update_shape(id: int, body: dict):
    """
    Updating shape size
    :param id:
    :param body:
    """
    update_shape = manager.update_shape(id, **body)
    if update_shape is None:
        raise HTTPException(status_code=404, detail="404")
    return update_shape.to_dict()


@app.delete("/shapes/{id}")
def delete_shape(id: int):
    """
    Deletes a shape by ID number
    :param id:
    :return: "shape delete"
    """
    delete_shape = manager.delete_shape(id)
    if delete_shape is False:
        raise HTTPException(status_code=404, detail="404 - Not found")
    return "shape delete"


@app.get("/shapes")
def return_all_shapes():
    """
    Displays all existing shapes
    :return: objects_dict
    """
    objects = manager.get_all_shapes()
    objects_dict = []
    for obj in objects:
        objects_dict.append(obj.to_dict())
    return objects_dict


@app.post("/shapes")
def add_shape(data: dict):
    """
    Add a new shape
    :param data:
    :return: into the json file
    """
    objects = manager.create_shape(data)
    return objects.to_dict()





if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)