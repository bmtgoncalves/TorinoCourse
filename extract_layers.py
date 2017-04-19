import json
import sys

data = json.load(open('GeoJSON/NUTS_RG_20M_2013.geojson'))
encoder = json.JSONEncoder()

for layer in range(0, 5):
	countries = {}

	countries["crs"] = data["crs"]
	countries["type"] = data["type"]
	countries["features"] = [] 

	for feat in data["features"]:         
		if feat["properties"]["STAT_LEVL_"] == layer:
			countries["features"].append(feat)

	if len(countries["features"]) > 0:
	    output = encoder.encode(countries)

	    fp = open("GeoJSON/layer_%02u.geojson" % layer, "w")
	    print(output, file=fp)
	    fp.close()

