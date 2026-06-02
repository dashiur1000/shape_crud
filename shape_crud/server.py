import uvicorn

from new_shape_manager import ShapeManager
from fastapi import FastAPI, HTTPException

app = FastAPI()
manager = ShapeManager()


@app.get("/shapes/{id}")
def return_shape(id: int):
    find = manager.find_id(id)
    if find is None:
        raise HTTPException(status_code=404, detail="404")
    return find.to_dict()


@app.put("/shapes/{id}")
def update_shape(id: int, data: dict):
    update_shape = manager.update_shape(id, **data)
    if update_shape is None:
        raise HTTPException(status_code=404, detail="404")
    return update_shape.to_dict()


@app.delete("/shapes/{id}")
def delete_shape(id: int):
    delete_shape = manager.delete_shape(id)
    if delete_shape is False:
        raise HTTPException(status_code=404, detail="404")
    return "shape delete"



@app.get("/shapes")
def return_all_shapes():
    objects = manager.get_all_shapes()
    objects_dict = []
    for obj in objects:
        objects_dict.append(obj.to_dict())
    return objects_dict


@app.post("/shapes")
def add_shape(data: dict):
    objects = manager.create_shape(data)
    return objects.to_dict()



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)