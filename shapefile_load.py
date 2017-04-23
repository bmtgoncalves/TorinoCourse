import sys
import shapefile
from shapely.geometry import shape

shp = shapefile.Reader(sys.argv[1])

print("Found", shp.numRecords, "records:")

pos = None
count = 0
for record in shp.records():
    print("  ", record[1])

    if record[1] == sys.argv[2]:
        pos = count

    count += 1

if pos is None:
    print(sys.argv[2], "not found in shapefile", file=sys.stderr)
    sys.exit()

print("Using", sys.argv[2], "...", file=sys.stderr)

manhattan = shape(shp.shapes()[pos])

print(manhattan.contains(manhattan.centroid))