"""
Usage:
curl -XPOST http://localhost:8888/api/v0/house_value -d @sample_request.json
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from tornado_sandbox.views import HelloWorld, MakePrediction
import numpy as np

define('port', default=8888, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    coefs = np.random.normal(size=8)
    app = Application([
        ('/', HelloWorld),
        ('/api/v0/house_value', MakePrediction, {"coefs": coefs}),
        ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()
