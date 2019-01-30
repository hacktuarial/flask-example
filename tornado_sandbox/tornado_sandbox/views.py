# https://opensource.com/article/18/6/tornado-framework
from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    def get(self):
        self.write("hello world")

class MakePrediction(RequestHandler):
    def post(self, data):
        pred = pipeline.predict(data)
        self.write({'predicted_housing_value': pred})
