import matplotlib.pyplot as plt
import numpy as np
import json
import sys

data = json.load(open(sys.argv[1]))

def get_bbox(country):
	maxLat = None
	maxLon = None
	minLat = None
	minLon = None

	for polygon in country["geometry"]["coordinates"]:
		coords = np.array(polygon)[0]

		curMaxLat = np.max(coords.T[1])
		curMinLat = np.min(coords.T[1])

		curMaxLon = np.max(coords.T[0])
		curMinLon = np.min(coords.T[0])

		if maxLat is None or curMaxLat > maxLat:
			maxLat = curMaxLat

		if maxLon is None or curMaxLon > maxLon:
			maxLon = curMaxLon

		if minLat is None or curMinLat < minLat:
			minLat = curMinLat

		if  minLon is None or curMinLon < minLon:
			minLon = curMinLon

	return maxLat, maxLon, minLat, minLon

def plot_country(country):
	for polygon in country["geometry"]["coordinates"]:
		coords = np.array(polygon[0])
		plt.plot(coords.T[0], coords.T[1])

for country in data["features"]:
	plot_country(country)

maxLat, maxLon, minLat, minLon = 73, 88, -24, -94 #get_bbox(country)

plt.xlim(minLon, maxLon)
plt.ylim(minLat, maxLat)

plt.show()