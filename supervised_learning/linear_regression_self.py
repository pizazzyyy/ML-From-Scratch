from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import sys
import os
import math
# Import helper functions
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_parth + "/../utils")
from data_operation import mean_squared_error
from data_manipulation imprt train_test_split
