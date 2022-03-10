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

        # 인접 노드 구하자
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and visited[i] == False:
                visited[i] = True
                counted[i] = True
                queue.append(i)
    return visited

n, m = map(int, input().split())

edges = []
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1


count = 0
visited = [False] * (n+1)
counted = [False] * (n+1)

for v in range(1,n+1):
    if counted[v] == False:
        bfs(graph, v, visited)
        count += 1

print(count)