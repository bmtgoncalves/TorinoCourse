import github
from github_accounts import accounts

token = accounts["social"]

client = github.Github(token, per_page=100)

screen_name = "torvalds"

user = client.get_user(screen_name)

follow_count = 0

for follow in user.get_followers():
    print(follow_count, follow.name)

    follow_count += 1

    if follow_count == 10:
        break
