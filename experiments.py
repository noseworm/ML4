import csv
import numpy as np
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

def loadData(filename):
	data = np.genfromtxt(filename, delimiter=',', dtype=None, loose=True, invalid_raise=False, skip_header=1)
	return data
