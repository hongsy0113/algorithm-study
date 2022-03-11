import sys
from collections import deque

## dfs 정의
def dfs(graph, v, visited):
    visited[v] = True
    # print(v)
    if not visited[graph[v]]:
        dfs(graph, graph[v], visited)


## 입력 파트
T = int(sys.stdin.readline())

graph = [[]] * T
counts = [0] * T
for i in range(T):
    n = int(sys.stdin.readline())
    graph[i] = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(T):
    visited = [False] * (len(graph[i]) + 1)
    for v in graph[i][1:]:
        if not visited[v]:
            dfs(graph[i], v, visited)
            counts[i] += 1

for count in counts:
    print(count)
