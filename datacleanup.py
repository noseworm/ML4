import numpy as np
import csv
import json
import urllib2
import urllib

def loadData(filename):
	data = []
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
        		data.append(row)
	#data = np.genfromtxt(filename, delimiter=',', dtype=None, loose=True, invalid_raise=False)
	return data

def saveData(data, filename):
	writer = csv.writer(open(filename, 'w'), delimiter='|')
	for row in data:
		writer.writerow(row)

def getURL(address):
	address = address.replace(" ", "+")
	return "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyA6_ynPzZCQLtdBYNQmszxBlP7iFd5TjWQ"

def getCoordinates(address):
	url = getURL(address)
	#print url
	data = json.load(urllib2.urlopen(url))
	#print data
	if(data["status"] == "OK"):
		lat = data["results"][0]["geometry"]["location"]["lat"]
		lng = data["results"][0]["geometry"]["location"]["lng"]
		return (lat, lng)
	else:
		return ("","")

data = loadData("Dec1Data.csv")
print len(data)
final_data = []
for d in data:
	print len(final_data)
	if(d[5] == 0 or d[5] == ""):
		(lat, lng) = getCoordinates(d[10])
		d[5] = lng
		d[11] = lat
	final_data.append(d)
	
saveData(final_data, "final_data_fixed-cleanDec.csv")
		