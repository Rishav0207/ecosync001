# predictor.py
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_risk(values):
    X = np.array(range(len(values))).reshape(-1, 1)
    y = np.array(values)

    model = LinearRegression()
    model.fit(X, y)

    future = model.predict([[len(values) + 5]])
    return future[0]
