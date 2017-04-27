import github
from github_accounts import accounts
import networkx as NX

token = accounts["social"]

client = github.Github(token, per_page=100)

screen_name = "ptwobrussell"
repository_name = "Mining-the-Social-Web"

user = client.get_user(screen_name)
repo = user.get_repo(repository_name)

G = NX.DiGraph()

for commit in repo.get_commits():
    for parent in commit.parents:
        G.add_edge(parent.sha, commit.sha)

print(G.number_of_nodes(), G.number_of_edges())