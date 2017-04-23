import numpy as np
import json
import gzip
import matplotlib.pyplot as plt

data = json.load(open('Europe_NUTS.geojson'))

countries = {}

countries["crs"] = data["crs"]
countries["type"] = data["type"]
countries["features"] = [] 

for feat in data["features"]:         
    if feat["properties"]["STAT_LEVL_"] == 0:
    	countries["features"].append(feat)

print(countries["features"][9]["properties"]["NUTS_ID"])

spain = countries["features"][9]

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

		#print(coords)

		print(coords[-1])
		print(curMaxLat, curMaxLon, curMinLat, curMinLon)

	return maxLat, maxLon, minLat, minLon

def plot_country(country):
	for polygon in country["geometry"]["coordinates"]:
		coords = np.array(polygon)[0]

		plt.plot(coords.T[0], coords.T[1])

	maxLat, maxLon, minLat, minLon = get_bbox(spain)

	plt.xlim(minLon, maxLon)
	plt.ylim(minLat, maxLat)

	plt.show()

plot_country(spain)