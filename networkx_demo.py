import networkx as NX
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def BarabasiAlbert(N=1000000):
	G = NX.Graph()

	nodes = range(N)
	G.add_nodes_from(nodes)

	edges = [0,1,1,2,2,0]

	for node_i in range(3, N):
		pos = np.random.randint(len(edges))
		node_j = edges[pos]

		edges.append(node_i)
		edges.append(node_j)

	edges = zip(nodes, edges[1::2])

	G.add_edges_from(edges)

	return G

net = BarabasiAlbert()

degrees = net.degree()
Pk = np.array(list(Counter(degrees.values()).items()))

plt.loglog(Pk.T[0], Pk.T[1], 'b*')
plt.xlabel('k')
plt.ylabel('P[k]')
plt.savefig('Pk.png')
plt.close()

print("Number of nodes:", net.number_of_nodes())
print("Number of edges:", net.number_of_edges())
print("Is Connected?", NX.is_connected(net))
print("Is Directed?", NX.is_directed(net))