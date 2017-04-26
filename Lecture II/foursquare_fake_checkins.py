import twitter
import foursquare
from  twitter_accounts import accounts as accounts_tw
from  foursquare_accounts import accounts as accounts_4sq
from urllib import parse
import posixpath

app_tw = accounts_tw["social"]

auth = twitter.oauth.OAuth(app_tw["token"],
                           app_tw["token_secret"],
                           app_tw["api_key"],
                           app_tw["api_secret"])

stream_api = twitter.TwitterStream(auth=auth)

print("Instanciated Twitter API")

app_4sq = accounts_4sq["tutorial"]

client = foursquare.Foursquare(client_id=app_4sq["client_id"],
                               client_secret=app_4sq["client_secret"])

client.set_access_token(app_4sq["access_token"])

print("Instanciated Foursquare API")

query = "#4sq #checkin"

stream_results = stream_api.statuses.filter(track=query)

users = {}

for tweet in stream_results:
	print(tweet["id"])
	for url in tweet["entities"]["urls"]:
		expanded_url = url["expanded_url"]

		parsed = parse.urlparse(expanded_url)

		if parsed.netloc == '4sq.com':
			twitter_user = tweet["user"]["screen_name"]

			if twitter_user not in users:
				results = client.users.search({"twitter": twitter_user})

				foursquare_user = results["results"][0]
				users["twitter_user"] = foursquare_user
			else:
				foursquare_user = users["twitter_user"]

			req = request.get(expanded_url)
			final_url = req.url

			parsed_final = parse.urlparse(final_url)
			venue_id = posixpath.basename(parsed_final.path)

			venue = client.venues(venue_id)

			print(foursquare_user["firstName"], foursquare_user["lastName"], "checked in at", venue["venue"]["name"], "on", tweet["created_at"])



