import twitter
from twitter_accounts import accounts
import sys
import gzip
import json

app = accounts["social"]

auth = twitter.oauth.OAuth(app["token"],
                           app["token_secret"],
                           app["api_key"],
                           app["api_secret"])

stream_api = twitter.TwitterStream(auth=auth)

query = "-74,40,-73,41"  # NYC

stream_results = stream_api.statuses.filter(locations=query)

tweet_count = 0

fp = open("NYC.json", "w")
encoder = json.JSONEncoder()

for tweet in stream_results:
    try:
        tweet_count += 1
        print (tweet_count, tweet["id"])

        print(tweet, file=fp)
    except:
        pass

    if tweet_count % 10000 == 0:
        print(tweet_count, file=sys.stderr)
        break

fp.close()
