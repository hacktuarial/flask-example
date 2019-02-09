import numpy as np
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge


def model():
    """Simple example of scikit-learn pipeline"""
    p = Pipeline([("preprocess", StandardScaler()), ("model", Ridge(alpha=10.))])
    return p


def train():
    # induce some randomness to illustrate model refreshing
    data = fetch_california_housing()
    X = data.data
    index = np.random.randint(low=0, high=X.shape[0], size=X.shape[0])
    pipeline = model()
    pipeline.fit(X=X[index, :], y=data.target[index])
    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(pipeline, f)


if __name__ == "__main__":
    train()
