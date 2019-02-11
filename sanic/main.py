"""
curl localhost:8000/api/v0/house_value -d @flask/sample_request.json
"""
import time
import pickle

from sanic import Sanic
from sanic.response import json
import numpy as np

MODEL_FILE = "artifacts/model.pkl"


def load_model():
    global model
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)


app = Sanic()


@app.route("/api/v0/house_value", methods=["POST"])
async def test(request):
    x = np.array(request.json).reshape(1, -1)
    return json({"predicted_housing_value": model.predict(x)[0]})

@app.route("/api/v0/update", methods=["GET"])
def reload(request):
    load_model()
    return json({"updated_at": time.time()})


if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, workers=2)
