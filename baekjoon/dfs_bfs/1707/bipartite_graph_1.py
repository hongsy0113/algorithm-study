import sys
from collections import deque

# bfs 함수 정의
def bfs_and_bipartite(graph, start, visited, colored):
    queue = deque([start])
    visited[start] = True
    colored[start] = 1
    while queue:
        v = queue.popleft()
        #print(v, end=' ')
        for i in graph[v]:
            # 지금 칠할 차례인 색과 이미 칠해진 인접노드의 색이 같으면 return False
            if colored[v] % 2 == colored[i]%2:
                return 'NO'

            # 인접 노드 색칠
            colored[i] = colored[v] + 1

            if visited[i] == False:
                visited[i] = True

                queue.append(i)
    return 'YES'

k = int(sys.stdin.readline())

graph = [[]] * k

for i in range(k):
    v_num, e_num = map(int, sys.stdin.readline().split())
    graph[i] =  [[] for _ in range(v_num+1)]
    for j in range(e_num):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[i][v1].append(v2)
        graph[i][v2].append(v1)

for i in range(k):
    # 각 테스트케이스 별로 탐색 시작
    # 각 테스트케이스 별로 start 노드 지정
    for j in range(len(graph[i])):
        if graph[i][j]:
            start = graph[i][j][0]
            break
    visited = [False] * len(graph[i])
    colored = [0] * len(graph[i])
    print(bfs_and_bipartite(graph[i], start, visited, colored))
