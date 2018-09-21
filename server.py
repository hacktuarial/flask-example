"""
Minimal API to serve predictions from a scikit-learn model with Flask
Usage:
    curl -i -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v0/house_value -d @sample_request.json

"""
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
app.vars = {}


@app.route('/api/v0/house_value', methods=['POST'])
def predict():
    x = np.array(request.json).reshape(1, -1)
    pred = app.vars['model'].predict(x)[0]
    return jsonify({
        'predicted_housing_value': pred
    })


if __name__ == '__main__':
    model_file = 'model.pkl'
    with open(model_file, 'rb') as f:
        app.vars['model'] = pickle.load(f)
    app.run(debug=True, extra_files=[model_file])
