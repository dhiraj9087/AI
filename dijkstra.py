import heapq
import sys

def dijkstra(graph, source):
    vertices = len(graph)
    visited = [False] * vertices
    distance = [sys.maxsize] * vertices
    distance[source] = 0
    pq = [(0, source)]  # Priority queue to store (distance, vertex) pairs

    while pq:
        # print(pq)
        dist, u = heapq.heappop(pq)
        # print(dist,u)
        if visited[u]:
            continue

        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and dist + weight < distance[v]:
                distance[v] = dist + weight
                heapq.heappush(pq, (distance[v], v))

    return distance


def fun(graph,source):
    ver = len(graph)
    dis = [float('inf')]*(ver)
    vis=[False]*ver
    dis[source]=0
    pq=[(0,source)]

    while pq:
        dist,u=heapq.heappop(pq)
        if vis[u]:
            continue
        vis[u]=True

        for v,wei in graph[u]:
            if not vis[v] and dist+wei<dis[v]:
                dis[v]=dist+wei
                heapq.heappush(pq,(dis[v],v))
    return dis


graph = [
    [(1,5), (2, 8)],     # Node 0: (neighbor, weight)
    [(0, 5), (2, 9), (3, 2)], 
    [(0, 8), (1, 9), (3,6)], 
    [(1,2), (2,6)]
]

source_node = 0
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source node {}:".format(source_node))
for i, dist in enumerate(shortest_distances):
    print("To node {}: {}".format(i, dist))
