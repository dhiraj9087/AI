def create_adj_list(edges):
    # Create an adjacency list from the given edges
    adj_list = {}
    for u, v, weight in edges:
        if u not in adj_list:
            adj_list[u] = {}
        if v not in adj_list:
            adj_list[v] = {}
        adj_list[u][v] = weight
        adj_list[v][u] = weight  # Since the graph is undirected
    return adj_list

def prim(graph):
    mst = set()  # Set to store vertices in the MST
    start_vertex = 0
    mst.add(start_vertex)
    mst_edges = []  # List to store MST edges
    total_weight = 0  # Variable to store the total weight of MST
    
    while len(mst) < len(graph):
        min_edge, min_weight = float('inf'), float('inf')
        next_vertex = None
        
        # Find the minimum weight edge connecting the MST to the fringe vertices
        for vertex in mst:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in mst and weight < min_weight:
                    min_edge, min_weight = (vertex, neighbor), weight
                    next_vertex = neighbor

        # Add the chosen edge to the MST
        mst.add(next_vertex)
        mst_edges.append(min_edge)
        total_weight += min_weight

    return mst_edges, total_weight

# Given edges
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]

# Create adjacency list
graph = create_adj_list(edges)

# Find minimum spanning tree edges and total weight
minimum_spanning_tree_edges, total_weight = prim(graph)
print("Minimum Spanning Tree edges:")
for u, v in minimum_spanning_tree_edges:
    print(f"{u} -- {v}")

print("Total weight of the Minimum Spanning Tree:", total_weight)
