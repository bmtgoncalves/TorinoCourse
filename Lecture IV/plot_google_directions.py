import googlemaps
from google_accounts import accounts
import matplotlib.pyplot as plt

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

directions = gmaps.directions((45.485895, 9.204283),(45.067450, 7.685880))

steps = directions[0]["legs"][0]["steps"]

for step in steps:
	start = (step["start_location"]["lng"], step["start_location"]["lat"])
	stop = (step["end_location"]["lng"], step["end_location"]["lat"])

	plt.plot([start[0], stop[0]], [start[1], stop[1]])

plt.savefig('MiTo.png')