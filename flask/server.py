"""
Minimal API to serve predictions from a scikit-learn model with Flask
Usage:
    curl -i -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v0/house_value -d @sample_request.json
    curl -X POST http://127.0.0.1:5000/api/v0/update

"""
import time
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
app.vars = {}
MODEL_FILE = "../artifacts/model.pkl"


@app.before_first_request
@app.route("/api/v0/update", methods=["POST"])
def update():
    with open(MODEL_FILE, "rb") as f:
        app.vars["model"] = pickle.load(f)
    return jsonify({"updated_at": time.time()})


@app.route("/api/v0/house_value", methods=["POST"])
def predict():
    x = np.array(request.json).reshape(1, -1)
    pred = app.vars["model"].predict(x)[0]
    return jsonify({"predicted_housing_value": pred})


if __name__ == "__main__":
    app.run(debug=False, extra_files=[MODEL_FILE])
