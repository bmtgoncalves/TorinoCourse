import github
from github_accounts import accounts

token = accounts["social"]

client = github.Github(token, per_page=100)

screen_name = "torvalds"
repository_name = "linux"

user = client.get_user(screen_name)
repo = user.get_repo(repository_name)

user_count = 0

for user in repo.get_stargazers():
    print user_count, user.name

    user_count += 1

    if user_count == 10:
        break
