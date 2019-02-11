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


@routes.post("/api/v0/house_value")
async def predict(request):
    req = await request.json()
    x = np.array(req.get("x")).reshape(1, -1)
    return web.json_response({"predicted_housing_value": model.predict(x)[0]})


@routes.get("/")
async def hello(request):
    return web.Response(text="Hello, world")


update(request=None)
app = web.Application()
app.add_routes(routes)
web.run_app(app, port=5001)
