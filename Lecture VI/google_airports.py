import googlemaps
from google_accounts import accounts
import time
import sys

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

line_count = 0
for line in open("flights/L_AIRPORT_ID.csv"):
	fields = line.strip()[:-1].split(',')
	time.sleep(1)
	line_count += 1

	if line_count > 1:
		try:
			airport_id = fields[0]
			airport_name = ", ".join(fields[2:])
			print(line_count, airport_id, file=sys.stderr)
			geocode_result = gmaps.geocode(airport_name)

			print(airport_id[1:-1], geocode_result[0]["geometry"]["location"]["lat"], geocode_result[0]["geometry"]["location"]["lng"])

		except:
			pass
