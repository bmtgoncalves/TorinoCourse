import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

reverse_result = json.load(open('reverse.json')) #gmaps.reverse_geocode((40.6413111,-73.77813909999999))

plt.figure()
plt.xlim(-130,-65)
plt.ylim(20,50)
currentAxis = plt.gca()


for result in reverse_result:
	viewport = result["geometry"]["viewport"]
	xy = (viewport['southwest']['lng'], viewport['southwest']['lat'])
	width = viewport['northeast']['lng']-viewport['southwest']['lng']
	height = viewport['northeast']['lat']-viewport['southwest']['lat']
	
	currentAxis.add_patch(patches.Rectangle(xy, width, height, alpha=.1))

plt.savefig('reverse.png')