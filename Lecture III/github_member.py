import gzip
import json
import networkx as NX

filename = "data/2015-01-01-15.json.gz"

G = NX.DiGraph()

for line in gzip.open(filename):
    event = json.loads(line.strip().decode())

    if event["type"] == "MemberEvent":
        actor = event["actor"]["login"]
        member = event["payload"]["member"]["login"]

        G.add_edge(actor, member)

print(G.number_of_nodes(), G.number_of_edges())
