"""
Sync server:
    45.7, 50.0, 
Async server:
    It took 57.446223 seconds to do 100 requests
"""
import numpy as np
import requests
import time
import multiprocessing as mp


def get_prediction(i):
    resp = requests.post("http://localhost:8888/api/v0/house_value",
            json={"row_index": int(i)})
    result = {**resp.json(), **{"row_index": i}}
    print(result)
    return result

if __name__ == '__main__':
    indexes = np.random.randint(low=0, high=20000, size=100)
    p = mp.Pool(4)
    tic = time.perf_counter()
    p.map(get_prediction, indexes)
    toc = time.perf_counter()
    print("It took %f seconds to do %d requests" % (toc-tic, len(indexes)))
