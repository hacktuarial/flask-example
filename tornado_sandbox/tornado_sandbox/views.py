# https://opensource.com/article/18/6/tornado-framework
import numpy as np
import json
from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    def get(self):
        self.write("hello world")

class MakePrediction(RequestHandler):
    SUPPORTED_METHODS = ["POST"]

    def initialize(self, model, data):
        self.model = model
        self.data = data

    def set_default_headers(self):
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def post(self):
        row_index = int(json.loads(self.request.body)["row_index"])
        # should verify it's in bounds for self.data

        # pretend this is a database call
        x = self.data[row_index, :].reshape(1, -1)

        # this part is CPU-bound
        output = {"predicted_housing_value": self.model.predict(x)[0]}
        self.write(output)
