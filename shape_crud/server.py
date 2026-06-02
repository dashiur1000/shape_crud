import uvicorn

from new_shape_manager import ShapeManager
from fastapi import FastAPI, status

app = FastAPI()
manager = ShapeManager()

@app.get("/shapes")
def return_all_shapes():
    objects = manager.get_all_shapes()
    objects_dict = []
    for obj in objects:
        objects_dict.append(obj.to_dict())
    return objects_dict


# @app.get("/shapes/{id}")
# def return_shape(id_num):
#     data = manager.find_id(id_num)
#     return data


@app.post("/shapes")
def add_shape(data: dict):
    objects = manager.create_shape(data)
    return objects


@app.put("/shapes/{id}")
def update_shape(id_number: int):
    manager.update_shape(id_number)


@app.delete("/shapes/{id}")
def delete_shape(id_number: int):
    manager.delete_shape(id_number)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)