import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://bit.ly/GoogleScholar"

req = requests.get(url)
print("Status code:", req.status_code)
print("Server Header Information:")
pprint(req.headers)

new_url = req.url

print(url, "redirected to", new_url)