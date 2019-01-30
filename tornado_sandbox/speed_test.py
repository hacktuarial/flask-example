import numpy as np
import requests
import time


def get_prediction(i):
    return requests.post("http://localhost:8888/api/v0/house_value",
            data={"row_index": i})

if __name__ == '__main__':
    indexes = np.random.randint(low=0, high=20000, size=10)
    tic = time.perf_counter()
    for i in indexes:
        pred = get_prediction(i).json()["predicted_housing_value"]
        print("index = %d, pred=%f" % (i, pred))
    toc = time.perf_counter()
    print("It took %f seconds to do %d requests" % (toc-tic, len(indexes)))
