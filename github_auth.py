import github

accounts = {
    "social" : TOKEN,               
}

token = accounts["social"]

client = github.Github(token, per_page=100)
