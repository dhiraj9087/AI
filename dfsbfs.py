def dfs(graph, v, visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    print(v, end=' ')
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    

    
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph={}
n=int(input("enter number of edges"))
for i in range(n):
    u,v=map(int,input("ENter source and destination").split())
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[] 
    graph[u].append(v)
start_node=int(input("enter start node"))


print("DFS Traversal:")
dfs(graph, start_node)
print("\nBFS Traversal:")
bfs(graph, start_node)