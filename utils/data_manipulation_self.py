from __future__ import division
import numpy as np
import math
import sys

# Split the data into train and test sets
def train_test_split(X, y, test_size=0.5, shuffle=True):
    if shuffle:
        X, y = shuffle_data(X, y)
        # Split the training data from test data in the retio specified in
        # test_size
        split_i = len(y) - int(len(y) // (1 / test_size))
        x_tain, x_test = X[:split_i], X[split_i:]
        y_train, y_test = y[:split_i], y[split_i:]

        return x_train, x_test, y_train, y_test

def shuffle_data(X, y):
    # Concatenate x and y and do a random shuffle_data
    X_y = np.concatenate((X, y.reshape((1, len(y))).T), axis=1)
