import gzip
import json
import github
from github_accounts import accounts
import sys

token = accounts["social"]

client = github.Github(token, per_page=100)

filename = "2015-01-01-15.json.gz"

for line in gzip.open(filename):
    event = json.loads(line.strip())

    if event["type"] == "PushEvent":
        user_name, repo_name = event["repo"]["name"].split('/')

        try:
            user = client.get_user(user_name)
            repo = user.get_repo(repo_name)

            for commit in event["payload"]["commits"]:
                commit_id = commit["sha"]

                commit = repo.get_commit(commit_id)

                for parent in commit.parents:
                    print commit_id, parent.sha
        except Exception, e:
            print >> sys.stderr, "Error processing", event["repo"]["name"], e.status