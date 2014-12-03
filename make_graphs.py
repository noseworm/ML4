import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def get_missing_data_plot():
	N = 5
	values = [276, 1492, 1944, 3531, 5276]
	indices = np.arange(N)
	width = 1
	fig, ax = plt.subplots()
	rects1 = ax.bar(indices, values, width, color='r')
	ax.set_ylabel('Number of Samples with Missing Data')
	ax.set_xlabel('Features')
	ax.set_xticks(indices+width/2.0)
	ax.set_xticklabels(('num_bath', 'num_bed', 'year_built', 'living_area', 'num_room'))
	plt.show()
	
def get_knn_plot():
	xs = [1, 5, 10, 25, 50]
	ys_remove = [53237.9329566,45209.7125948,45960.5608356,48585.3941053,52868.8219684]
	ys_mean = [78259.1829037,68398.7744757,68553.5061504,71210.8411428,73907.104319]
	ys_em = [73183.8356913,62981.6363301,63364.5720675,65266.4795907,67519.626988]
	plt.plot(xs, ys_remove, 'r-', label='Missing Data Removed')
	plt.plot(xs, ys_mean, 'g-', label='Replaced with Mean')
	plt.plot(xs, ys_em, 'b-', label='Estimated with EM')
	plt.xlabel('k')
	plt.ylabel('Mean Absolute Error ($)')
	plt.legend(loc=1)
	plt.show()
	
def get_lasso_plot():
	xs = [0.1, 0.3, 1, 3, 10, 33, 100, 333]
	ys_remove = [44485.1309585,44482.8773212,44477.933003,44469.7127377,44457.7574089,44402.6798218,44315.0980156,44373.1985871]
	ys_mean = [61080.0592756,61079.9729209,61079.55998,61079.4406952,61078.1489281,61079.6276681,61109.5265341,61279.8498369]
	ys_em = [64640.7222531,64640.4215938,64639.3641086,64636.8840664,64629.504159,64645.8140952,64682.0576915,64895.4317682]
	plt.plot(xs, ys_remove, 'r-', label='Missing Data Removed')
	plt.plot(xs, ys_mean, 'g-', label='Replaced with Mean')
	plt.plot(xs, ys_em, 'b-', label='Estimated with EM')
	plt.xlabel('lambda')
	plt.ylabel('Mean Absolute Error ($)')
	plt.legend(loc=1)
	plt.show()
	
def get_predictor_plot():
	N = 39
	lr = [  1.08197251e+05,   9.60088905e+04,   8.58011100e+04,   8.31671320e+04,
	7.33272210e+04,  -7.73877523e+04,  -3.69113852e+05,   1.09276352e-11,
	8.91227500e-10,  -2.08906362e-10,  -5.88239263e-10,   1.73011227e-09,
	-7.10038651e-10,  -4.28579060e-10,   3.00784531e+03,  -5.31797692e+01,
	1.91712200e+05,  -3.76388484e+05,   5.44170611e+03,   4.79185886e+04,
   2.15370420e+03,  -6.51798075e+04,   2.77656435e+05,  -1.74901149e-09,
   -1.06340144e+05,  -1.06136483e+05,   4.95483614e+03,  -4.22223624e+03,
   -4.79999952e+02,  -1.30732625e+02,  -5.83508682e+03,   1.31122271e+03,
   2.77531272e+02,   4.05169412e+03,  -6.08578453e+01,  -1.58474862e+02,
   -3.00240779e+03,  -1.23723645e+03,  -2.28122559e+01]
	lasso = [  2.47231777e+04,   1.26634273e+04,   2.14916632e+03,  -0.00000000e+00,
    -1.00570952e+04,  -1.01493343e+05,  -4.56049174e+04,   0.00000000e+00,
    0.00000000e+00,   0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
    0.00000000e+00,   0.00000000e+00,   2.50798073e+03,  -1.16804277e+02,
    0.00000000e+00,  -1.69107205e+05,   5.00902654e+03,   4.79135606e+04,
    2.15179113e+03,   3.56159041e+04,   1.85463457e+05,   0.00000000e+00,
    -6.19454960e+02,  -2.73316324e+03,   4.94326277e+03,  -4.06644026e+03,
    -2.75025316e+02,   2.54211318e+02,  -6.94749372e+03,   1.19433679e+03,
    3.10920787e+02,   3.34011811e+03,   5.76752621e+02,  -9.24134414e+02,
    -3.67075195e+03,  -1.41949711e+03,  -3.11675320e+02]
	indices = np.arange(N)
	width = 0.3
	fig, ax = plt.subplots()
	rects1 = ax.bar(indices, lr, width, color='r')
	rects2 = ax.bar(indices+width, lasso, width, color='b')
	ax.set_ylabel('Parameter Estimate')
	ax.set_xlabel('Parameter Index')
	ax.set_xticks(indices+width/2.0)
	ax.legend( (rects1[0], rects2[0]), ('Linear Regression', 'Lasso Regression') )
	ax.set_xticklabels((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38))
	plt.show()
	
def get_linear_regression_plot():
	N = 3
	values = [63672.7573831, 61335.5504952, 44680.8178676]
	indices = np.arange(N)
	width = 1
	fig, ax = plt.subplots()
	rects1 = ax.bar(indices, values, width, color='r')
	ax.set_ylabel('Mean Absolute Error ($)')
	ax.set_xlabel('Missing Data Method')
	ax.set_xticks(indices+width)
	ax.set_xticklabels(('EM', 'Mean', 'Removal'))
	plt.show()
	
if __name__=='__main__':
	#get_knn_plot()
	#get_lasso_plot()
	#get_linear_regression_plot()
	get_predictor_plot()
