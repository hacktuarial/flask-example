"""
gunicorn main:my_web_app --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker --workers 2
"""
import time
import pickle

import numpy as np
from aiohttp import web


routes = web.RouteTableDef()


@routes.get("/api/v0/update")
def update(request):
    global model
    with open("../artifacts/model.pkl", "rb") as f:
        model = pickle.load(f)
    return web.Response(text="updated model at %f" % time.time())


@routes.get("/api/v0/house_value")
async def predict(request):
    # req = await request.json()
    # x = np.array(req.get("x")).reshape(1, -1)
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
    return web.json_response({"predicted_housing_value": model.predict(x)[0]})


@routes.get("/")
async def hello(request):
    return web.Response(text="Hello, world")


async def my_web_app():
    update(request=None)
    app = web.Application()
    app.add_routes(routes)
    return app
