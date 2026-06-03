# Github link:
# https://github.com/dashiur1000/shape_crud.git

import uvicorn
import logging

from new_shape_manager import ShapeManager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
manager = ShapeManager()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(r"C:\Users\dzs10\Desktop\IDF\project_3_shape\shape_crud\logs_file.log", mode="a")
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


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
    logger.info("Started calculating area of all shapes")
    area = manager.get_total_area()
    logger.info("Calculate all the areas of all the shapes together.")
    return area


@app.get("/shapes/{id}")
def return_shape(id: int):
    """
    Displays a certain shape
    :param id:
    :return: shape
    """
    logger.info("Search by ID")
    find = manager.find_id(id)
    if find is None:
        logger.error("The ID does not exist.")
        raise HTTPException(status_code=404, detail="not found")
    logger.info("Displays the specific shape")
    return find.to_dict()


@app.put("/shapes/{id}")
def update_shape(id: int, body: dict):
    """
    Updating shape size
    :param id:
    :param body:
    """
    logger.info("Activates the shape update function")
    update_shape = manager.update_shape(id, **body)
    if update_shape is None:
        logger.error("The shape does not exist.")
        raise HTTPException(status_code=404, detail="404")
    logger.info("The shape has been updated with the updated parameters.")
    return update_shape.to_dict()


@app.delete("/shapes/{id}")
def delete_shape(id: int):
    """
    Deletes a shape by ID number
    :param id:
    :return: "shape delete"
    """
    logger.info("Activates the shape delete function")
    delete_shape = manager.delete_shape(id)
    if delete_shape is False:
        logger.error("The shape does not exist.")
        raise HTTPException(status_code=404, detail="404 - Not found")
    logger.info("The shape has been deleted.")
    return "shape delete"


@app.get("/shapes")
def return_all_shapes():
    """
    Displays all existing shapes
    :return: objects_dict
    """
    logger.info("Activates the shape return shapes function")
    objects = manager.get_all_shapes()
    objects_dict = []
    for obj in objects:
        objects_dict.append(obj.to_dict())
    logger.info("All shapes are displayed.")
    return objects_dict


@app.post("/shapes")
def add_shape(data: dict):
    """
    Add a new shape
    :param data:
    :return: into the json file
    """
    logger.info("Activates the shape add shapes function")
    objects = manager.create_shape(data)
    logger.info("The new form has been inserted and updated.")
    return objects.to_dict()





if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)