from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

line_count = 0
edges = {}

for line in open("flights/4567008_T_T100D_MARKET_ALL_CARRIER.csv"):
	fields = line.strip().split(',')

	line_count += 1

	if line_count == 1:
		header = dict(zip([field[1:-1] for field in fields], range(len(fields))))
		continue

	node_i = line[header["ORIGIN_AIRPORT_ID"]]
	node_j = line[header["DEST_AIRPORT_ID"]]
	edge = (node_i, node_j)

	edges[edge] = edges.get(edge, 0) + 1

Pw = Counter(edges.values())
Pw = list(Pw.items())
Pw.sort(key=lambda x:x[0])

Pw = np.array(Pw)

fig, ax = plt.subplots()
ax.loglog(Pw.T[0], Pw.T[1], 'r-')
plt.savefig('Pw.png')

