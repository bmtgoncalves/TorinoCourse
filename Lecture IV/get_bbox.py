import numpy as np
import json
import gzip
import matplotlib.pyplot as plt

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
		coords = np.array(polygon)

		plt.plot(coords.T[0], coords.T[1])

	maxLat, maxLon, minLat, minLon = get_bbox(country)

	plt.xlim(minLon, maxLon)
	plt.ylim(minLat, maxLat)

data = json.load(open('geofiles/NUTS_RG_20M_2013.geojson'))

countries = {}

countries["crs"] = data["crs"]
countries["type"] = data["type"]
countries = {}

for feat in data["features"]:         
    if feat["properties"]["STAT_LEVL_"] == 0:
    	countries[feat["properties"]["NUTS_ID"]] = feat

country = countries["EL"]

plot_country(country)
plt.savefig('Greece.png')