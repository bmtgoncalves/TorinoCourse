import requests
from bs4 import BeautifulSoup

url = "http://www.bgoncalves.com/page.html"

request = requests.get(url)

soup = BeautifulSoup(request.text, "lxml")

print("The title tag is", soup.title)
print("The id of the div is", soup.div["id"])

soup.div["id"] = "new_id" 

print("And now it's", soup.body.div["id"])