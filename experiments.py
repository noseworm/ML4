import csv
import numpy as np
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import missingdata
import random

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

def runKFold(X, Y, k):
	kf = cross_validation.KFold(len(Y), n_folds=4)
	errors = []
	for train_index, test_index in kf:
		X_train, X_test = X[train_index], X[test_index]
		Y_train, Y_test = Y[train_index], Y[test_index]
		mse = runLinearRegression(X_train, Y_train, X_test, Y_test)
		errors.append(mse)
	return np.mean(errors)

def extractTestSet(X, Y, ratio):
	expected_size = len(x)*ratio
	test_set_X = []
	test_set_Y = []
	while(len(test_set_X) < expected_size):
		chosen_index = random.randint(0, len(X))
		test_set_X.append(X[chosen_index])
		test_set_Y.append(Y[chosen_index])
		del X[chosen_index]
		del Y[chosen_index]
	print "Length of TEST set = " + str(len(test_set_X))
	print "Length of TRAIN set = " + str(len(X))
	return (X, Y, test_set_X, test_set_Y)

def finalTest(regressor, test_X, test_Y):
	pred_Y = clf.predict(test_X)
	mse = getMeanError(pred_Y, test_Y)
	return mse

