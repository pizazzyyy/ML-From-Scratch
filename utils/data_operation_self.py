from __future__ import division
import numpy as np
import math
import sys


# Returns the mean squared error between y_true and y_pred
def mean_squared_error(y_ture, y_pred):
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse
