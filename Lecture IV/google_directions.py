import googlemaps
from google_accounts import accounts

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

directions = gmaps.directions((45.067450, 7.685880), (45.485895, 9.204283))

steps = directions[0]["legs"][0]["steps"]

for step in steps:
    print(step["html_instructions"])