import requests

data = {"shape_type": "square", "side": 80}
responses = requests.post("http://127.0.0.1:8001/shapes", json=data)

print(responses.json())