from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
map = Basemap()
map.drawcoastlines()
plt.savefig('basemap_demo.png')
