import sys
import shapefile
from shapely.geometry import shape, Point
import gzip

shp = shapefile.Reader('geofiles/nybb_15c/nybb_wgs84.shp')

recordDict = dict(zip([record[1] for record in shp.iterRecords()], range(shp.numRecords)))

manhattan = shape(shp.shape(recordDict["Manhattan"]))
fp = gzip.open("Manhattan_places.json.gz", "w")

for line in gzip.open("NYC.json.gz"):
    try:
        tweet = eval(line.strip())
        point = None

        if "coordinates" in tweet and tweet["coordinates"] is not None:
            point = Point(tweet["coordinates"]["coordinates"])
        else:
        	if "place" in tweet and tweet["place"]["bounding_box"] is not None:
        		bbox = shape(tweet["place"]["bounding_box"])
        		point = bbox.centroid

        if point is not None and manhattan.contains(point):
        	fp.write(line)

        if point is None:
        	print("Woot")
    except:
        pass

fp.close()