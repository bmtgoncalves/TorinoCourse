import numpy as np
import matplotlib.pyplot as plt
import shapefile

def load_asc(filename):
    fp = open(filename)

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

    return data, xllcorner, yllcorner, cellsize

def map_points(xllcorner, yllcorner, cellsize, nrows, x, y):
    x = int((x-xllcorner)/cellsize)
    y = (nrows-1)-int((y-yllcorner)/cellsize)

    return x, y

fig, ax = plt.subplots(1,1)
data, xllcorner, yllcorner, cellsize  = load_asc('../Lecture V/geofiles/US_pop.asc')
ax.imshow(np.log(data+1))

shp = shapefile.Reader('geofiles/48States/48States.shp')

pos = None
count = 0
for shape in shp.iterShapes():
        points = np.array(shape.points)
        parts = shape.parts
        parts.append(len(shape.points))

        for i in range(len(parts)-1):
            positions = []

            for j in range(parts[i+1]-parts[i]):
                x_orig = points.T[0][parts[i]+j]
                y_orig = points.T[1][parts[i]+j]
                x, y = map_points(xllcorner, yllcorner, cellsize, data.shape[0], x_orig, y_orig)
                positions.append([x, y])
            
            positions = np.array(positions)

            ax.plot(positions.T[0], positions.T[1], 'r-')


fig.savefig('US_overlap.png')

