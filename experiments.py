import csv
import numpy as np
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import missingdata

'''
Think it would be good to explore:
	- Linear Regression
	- Ridge Regression
	- ...

'''

def loadData(filename):
	data = np.genfromtxt(filename, delimiter=',', dtype=None, loose=True, invalid_raise=False, skip_header=1)
	return data

def runLinearRegression(X_train, Y_train, X_test, Y_test):
	lin = LinearRegression()
	lin.fit(X_train, Y_train)
	acc = clf.predict(X_test)
	MSE = getMeanError(acc, Y_test)
	return MSE

def runRidgeRegression(X_train, Y_train, X_test, Y_test, a):
	lin = Ridge(alpha=a)
	lin.fit(X_train, Y_train)
	acc = clf.predict(X_test)
	MSE = getMeanError(acc, Y_test)
	return MSE

def searchRidgeAlpha(X_train, Y_train, X_test, Y_test):
	alphas = []
	mses = []
	rs = range(1,150)
	rs = [r / 100 for r in rs]
	for alpha in rs:
		mse = runRidgeRegressio(X_train, Y_train, X_test, Y_test, alpha)
		alphas.append(alpha)
		mses.append(mse)
	return (alphas, mses)

def getBestRidgeAlpha(alphas, mses):
	minError = min(mses)
	index = mses.index(minError)
	return alphas[index]

kf = cross_validation.KFold(len(Y), n_folds=4)	