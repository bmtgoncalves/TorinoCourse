import gzip
import json

filename = "2015-01-01-15.json.gz"

for line in gzip.open(filename):
    event = json.loads(line.strip())

    if event["type"] == "CreateEvent":
        print "Create", event["repo"]["name"]
    elif event["type"] == "ForkEvent":
        print "Fork", event["payload"]["forkee"]["full_name"]

