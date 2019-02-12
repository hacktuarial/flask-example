# flask-example
Minimal example of serving a scikit-learn model over a Python server, using the following Python web frameworks
* Flask
* Tornado
* Sanic (Forthcoming)
* AIOHTTP (Forthcoming)

# Steps for flask example
1. Fit a scikit-learn model - I do some light preprocessing, then fit a simple ridge regression model on the California housing dataset.
`python train.py`
2. Run flask server `cd flask && python server.py`
3. Hit the server `curl -i -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v0/house_value -d @flask/sample_request.json`
4. Update the model by re-running step 1. This just takes a bootstrap sample, but in production, you might retrain in batch.
5. Tell the server to reload the model from disk
`curl -X POST http://127.0.0.1:5000/api/v0/update`
6. Re-run the curl request from step 3 and note that you get a different answer!

# Tornado Example
* A little more involved, to try to test the async capabilities of this framework

# Sanic
1. Start the server: `docker run --rm -v $(pwd):/root/sanic -p 8000:8000 -v /Users/timothysweetser/git/flask-example/artifacts:/root/sanic/artifacts -w /root/sanic tsweetser/sanic python main.py`
2. Hit the server with a sample request: `curl localhost:8000/api/v0/house_value -d @flask/sample_request.json`
3. Retrain the model: `python train.py`
4. Tell the server to reload the model: `curl localhost:8000/api/v0/update`
5. Rerun step 2 and note that you get a different answer!


# Aiohttp
* TODO

# Warning
* This is not a real production system - no error handling, data validation, authentication, logging, etc etc etc
* Please file an issue or make a PR if you see any glaring errors


# Benchmarks
```


## Sanic
```
$ wrk -c 2000 -d 60s -t 12 --latency http://localhost:8000/api/v0/house_value --timeout 5s
Running 1m test @ http://localhost:8000/api/v0/house_value
12 threads and 2000 connections
Thread Stats   Avg      Stdev     Max   +/- Stdev
Latency   850.17ms  353.58ms   3.49s    74.01%
Req/Sec   222.55    206.50     1.29k    82.83%
Latency Distribution
50%  834.74ms
75%  946.81ms
90%    1.27s
99%    1.93s
113287 requests in 1.00m, 16.21MB read
Socket errors: connect 0, read 2353, write 10, timeout 0
Requests/sec:   1884.95
Transfer/sec:    276.12KB
```
