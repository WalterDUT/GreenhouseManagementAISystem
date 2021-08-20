import numpy as np


def convertDataShape(data):
    maxX = 100.5
    minX = 25
    value = 1.0 * (float(data) - minX) / (maxX - minX)
    X = np.array([value]).reshape(1, -1)
    return X
