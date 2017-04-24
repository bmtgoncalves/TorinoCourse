import requests
from bs4 import BeautifulSoup

url = "https://www.instagram.com/p/BTG1PoGBbtf/"

jsfuncs = {
    "true": True,
    "false": False,
    "null": None
}

magic_string = "window._sharedData = "
offset = len(magic_string)

page = requests.get(url).content
soup = BeautifulSoup(page, "lxml")

scripts = soup.findAll("script")

for script in scripts:
    if script.text.startswith(magic_string):
        text = script.text[offset:-1]

        data = eval(text, jsfuncs)
        break

comments = data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["edges"]

for comment in comments:
	print(comment["node"]["owner"]["username"], "==>", comment["node"]["text"].encode('utf8','replace').decode())