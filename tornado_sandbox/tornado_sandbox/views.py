# https://opensource.com/article/18/6/tornado-framework
import numpy as np
import json
from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    def get(self):
        self.write("hello world")

class MakePrediction(RequestHandler):
    SUPPORTED_METHODS = ["POST"]

    def initialize(self, model):
        self.model = model

    def set_default_headers(self):
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def post(self):
        x = np.array(json.loads(self.request.body)["x"]).reshape(1, -1)
        output = {"predicted_housing_value": self.model.predict(x)[0]}
        self.write(json.dumps(output))
