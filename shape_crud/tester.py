import requests



data = {"shape_type": "square", "side": 70}
responses = requests.put("http://127.0.0.1:8000/shapes/1", json=data)