# https://opensource.com/article/18/6/tornado-framework
import time
import numpy as np
import json
from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    def get(self):
        self.write("hello world")


class MakePrediction(RequestHandler):
    SUPPORTED_METHODS = ["POST", "GET"]

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

    async def get(self):
        """Sync version"""
        x = np.array(
            [
                2.8333,
                52.0,
                5.473317865429235,
                1.37122969837587,
                1100.0,
                2.5522041763341066,
                33.34,
                -118.33,
            ]
        ).reshape(1, -1)
        # this part is CPU-bound
        output = {"predicted_housing_value": self.model.predict(x)[0]}
        self.write(output)
