from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    counted[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    counted[v] = True
    
    while queue:
        node = queue.popleft()
        visited[node] = True
        counted[node] = True

        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                counted[i] = True
                queue.append(i)
    return visited

n, m = map(int, input().split())

edges = []
graph = [[] for _ in range(n+1)]
for i in range(m):
    edges.append(list(map(int, input().split())))

for edge in edges:
    graph[edge[0]].append(edge[1]) 
    graph[edge[1]].append(edge[0])

count = 0
visited = [False] * (n+1)
counted = [False] * (n+1)

for v in range(1,n+1):
    if counted[v] == False:
        bfs(graph, v, visited)
        count += 1

print(count)