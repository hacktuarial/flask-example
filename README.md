# flask-example
Toy example of using flask for a data science API

# Steps
1. Fit a model - I do some light preprocessing, then fit a simple ridge regression model on the California housing dataset.
`python train.py`
2. Run flask server `python server.py`
3. Hit the server `curl -i -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v0/house_value -d @sample_request.json`
4. Update the model by re-running step 1. This just takes a bootstrap sample, but in production, you might retrain in batch.
5. Run the same curl request and note that you get a different answer! Unfortunately, this only works when `debug=True`.

# Warning
* This is not a real production system - no error handling, data validation, authentication, etc etc etc
* Please file an issue or make a PR if you see any glaring errors
