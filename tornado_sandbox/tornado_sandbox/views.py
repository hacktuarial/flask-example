# https://opensource.com/article/18/6/tornado-framework
import numpy as np
import json
from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    def get(self):
        self.write("hello world")

class MakePrediction(RequestHandler):
    SUPPORTED_METHODS = ["POST"]

    def initialize(self, coefs):
        self.coefs = coefs

    def set_default_headers(self):
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def post(self):
        data = json.loads(self.request.body)
        x = np.array(data["x"])
        # random_coefs = np.random.normal(size=len(x))
        output = {"predicted_housing_value": np.inner(x, self.coefs)}
        self.write(json.dumps(output))
