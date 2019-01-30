# https://opensource.com/article/18/6/tornado-framework
import time
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

    # async def get_x(self, row_index: int):
    #     """ async version
    #     pretend this is a database call to get the feature vector for user `row_index`"""
    #     # should verify it's in bounds for self.data
    #     time.sleep(np.random.uniform())
    #     x = self.data[row_index, :].reshape(1, -1)
    #     return x

    # async def post(self):
    #     row_index = int(json.loads(self.request.body)["row_index"])
    #     x = await self.get_x(row_index=row_index)
    #     # this part is CPU-bound
    #     output = {"predicted_housing_value": self.model.predict(x)[0]}
    #     self.write(output)

    def post(self):
        """Sync version"""
        row_index = int(json.loads(self.request.body)["row_index"])
        time.sleep(np.random.uniform())
        x = self.data[row_index, :].reshape(1, -1)
        # this part is CPU-bound
        output = {"predicted_housing_value": self.model.predict(x)[0]}
        self.write(output)
