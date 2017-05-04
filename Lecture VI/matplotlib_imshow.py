import numpy as np
import matplotlib.pyplot as plt

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

def save_asc(data, xllcorner, yllcorner, cellsize, filename):
    fp = open(filename, "w")

    nrows, ncols = data.shape

    print("ncols", ncols, file=fp)
    print("nrows", nrows, file=fp)
    print("xllcorner", xllcorner, file=fp)
    print("yllcorner", yllcorner, file=fp)
    print("cellsize", cellsize, file=fp)
    print("NODATA_value", "-9999", file=fp)

    for i in range(nrows):
        for j in range(ncols):
            print(("%u " % data[i, j]), end="", file=fp)

        print("\n", end="", file=fp)

    fp.close()

fig, ax = plt.subplots(1,1)
data, xllcorner, yllcorner, cellsize  = load_asc('../Lecture V/geofiles/US_pop.asc')
ax.imshow(np.log(data+1))

x1, y1 = map_points(xllcorner, yllcorner, cellsize, data.shape[0], -86.523435, 39.163355, )
x2, y2 = map_points(xllcorner, yllcorner, cellsize, data.shape[0], -84.404820, 33.761926, )

ax.plot([x1, x2], [y1, y2], 'r-')
fig.savefig('US_ASC.png')

