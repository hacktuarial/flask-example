"""
Usage:
curl -XPOST http://localhost:8000/api/v0/house_value -d @tornado_sandbox/sample_request.json
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from tornado import autoreload
from tornado_sandbox.views import HelloWorld, MakePrediction
import pickle
from sklearn.datasets import fetch_california_housing

define("port", default=8000, help="port to listen on")
MODEL_FILE = "../artifacts/model.pkl"


def start_server():
    """Construct and serve the tornado application."""
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    app = Application(
        [
            ("/", HelloWorld),
            (
                "/api/v0/house_value",
                MakePrediction,
                {"model": model, "data": fetch_california_housing().data},
            ),
        ]
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print("Listening on http://localhost:%i" % options.port)
    IOLoop.current().start()


if __name__ == "__main__":
    options.parse_command_line()
    autoreload.start()
    autoreload.watch(MODEL_FILE)
    start_server()
