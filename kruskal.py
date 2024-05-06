def find(parent, i):
    # Find the parent of the set i
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    # Union by rank
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
    print(parent,rank)
def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))

    edges.sort()  # Sort edges by weight
    # print(edges)
    mst_edges = []
    parent = [i for i in range(len(graph))]
    # print(parent)
    rank = [0] * len(graph)

    for edge in edges:
        weight, u, v = edge
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst_edges.append((u, v, weight))
            union(parent, rank, x, y)

    return mst_edges

# Given edges
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]

# Create adjacency list
graph = {}
for u, v, w in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  # Since the graph is undirected

# Find minimum spanning tree edges using Kruskal's algorithm
minimum_spanning_tree_edges = kruskal(graph)
print("Minimum Spanning Tree edges (Kruskal's algorithm):")
for u, v, w in minimum_spanning_tree_edges:
    print(f"{u} -- {v} Weight: {w}")
