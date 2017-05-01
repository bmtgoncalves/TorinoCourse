import googlemaps
from google_accounts import accounts

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

reverse_result = gmaps.reverse_geocode((40.6413111,-73.77813909999999))

for result in reverse_result:
	print(result["types"], result["formatted_address"])