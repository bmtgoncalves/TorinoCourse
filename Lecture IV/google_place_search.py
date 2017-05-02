import googlemaps
from google_accounts import accounts
import time

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

geocode_result = gmaps.places("pizza", (45.090219, 7.659144), 10000)
result = geocode_result["results"][0]
print(result["formatted_address"])

time.sleep(5)
page_token = geocode_result["next_page_token"]
geocode_result = gmaps.places(None, page_token=page_token)
result = geocode_result["results"][0]

print(result["formated_address"])

