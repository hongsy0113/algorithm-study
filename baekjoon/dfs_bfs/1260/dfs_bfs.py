from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        visited[node] = True
        print(node, end=" ")
        
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, input().split())

# list comprehension으로 빈 그래프 인접 리스트 초기화
graph = [[] for _ in range(n+1)]
edges = []

for i in range(m):
    edges.append(list(map(int, input().split())))

for edge in edges:
    graph[edge[0]].append(edge[1]) 
    graph[edge[1]].append(edge[0])

# 인접 리스트를 정렬함으로써 작은 번호의 노드가 먼저 선택될 수 있도록 함
graph = [sorted(adj_list) for adj_list in graph ] 

visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)