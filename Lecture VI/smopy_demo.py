import smopy
import matplotlib.pyplot as plt

map = smopy.Map(24.396308, -124.848974, 49.384358, -66.885444)
ax = map.show_mpl()
fig = plt.gcf()

x0, y0 = map.to_pixels(39.163355, -86.523435)
x1, y1 = map.to_pixels(33.761926, -84.404820)

ax.plot([x0, x1], [y0, y1], 'r-')
fig.savefig('US_OSM.png')