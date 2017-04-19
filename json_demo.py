import requests
import json

url = "http://www.bgoncalves.com/test.json"

request = requests.get(url)

data = json.loads(request.text)

for user in data:
    name = user["name"]

    for friend in user["friends"]:
        print(name, "->", friend["name"])