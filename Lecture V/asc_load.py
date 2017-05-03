import numpy as np
import matplotlib.pyplot as plt

def map_points(xllcorner, yllcorner, cellsize, nrows, x, y):
	x = int((x-xllcorner)/cellsize)
	y = (nrows-1)-int((y-yllcorner)/cellsize)

	return x, y

fp = open("geofiles/US_pop.asc")

ncols, count = fp.readline().split()
ncols = int(count)

nrows, count = fp.readline().split()
nrows = int(count)

xllcorner, value = fp.readline().split()
xllcorner = float(value)

yllcorner, value = fp.readline().split()
yllcorner = float(value)

cellsize, value = fp.readline().split()
cellsize = float(value)

NODATA_value, value = fp.readline().split()
NODATA_value = float(value)

data = []

for line in fp:
	fields = line.strip().split()
	data.append([float(field) for field in fields])


data = np.array(data)
data[data==NODATA_value] = 0

x = -74.243251
y = 40.730503

coord_x, coord_y = map_points(xllcorner, yllcorner, cellsize, nrows, x, y)
print(data[coord_y, coord_x])

plt.imshow(np.log(data+1))
plt.colorbar()
plt.savefig('US_pop.png')
plt.close()