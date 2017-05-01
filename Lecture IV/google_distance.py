import googlemaps
from google_accounts import accounts
from pprint import pprint

app = accounts["torino"]
gmaps = googlemaps.Client(key=app["api_key"])

origins = [(45.485895, 9.204283), (41.912199, 12.499857)]
destinations = [(45.067450, 7.685880), (43.775475, 11.257102)]

matrix = gmaps.distance_matrix(origins, destinations)

pprint(matrix)