from  foursquare_accounts import accounts
from urllib import parse
import posixpath
import requests

app = accounts["tutorial"]

url_base = "https://api.foursquare.com/v2/checkins/resolve?shortId=%s&oauth_token=%s&v=20160912"

swarm_url = "https://www.swarmapp.com/c/j0cBYuhNHki"
parsed_url = parse.urlparse(swarm_url)
short_id = posixpath.basename(parsed_url.path)

url = url_base % (short_id, app["access_token"])

req = requests.get(url)

checkin = req.json()["response"]["checkin"]
checkin_id = checkin["id"]
user_name = checkin["user"]["firstName"]

print(short_id, ":", checkin_id, "was made by", user_name)