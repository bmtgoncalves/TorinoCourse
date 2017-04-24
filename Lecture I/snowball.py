import networkx as NX

def snowball(net, seed, max_depth = 3, maxnodes=1000):
    seen = set()
    queue = set()

    queue.add(seed)
    queue2 = set()

    for _ in range(max_depth+1):
	    while queue:
	        user_id = queue.pop()
	        seen.add(user_id)

	        NN = net.neighbors(user_id)

	        for node in NN:
	            if node not in seen:
	                queue2.add(node)

	    queue.update(queue2)
	    queue2 = set()

    return seen

net = NX.connected_watts_strogatz_graph(10000, 4, 0.01)
neve = snowball(net, 0)

print(neve)
