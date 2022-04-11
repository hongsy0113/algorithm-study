import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, k, graph, visited):
    visited[start] = True
    queue = deque([(start, 0)])
    result = []
    while queue:
        v, depth = queue.popleft()
        # depth 가 k 라면 count 를 증가하고 더이상 enqueue하지 않는다.
        if depth == k:
            result.append(v)
            continue
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, depth+1))
                visited[i] = True
    return result

def solution(n, k, x, graph):
    visited = [False] * (n+1)
    answer = bfs(x, k, graph, visited)

    if answer:
        answer.sort()
        for city in answer:
            print(city)
    else:
        print(-1)   
    return 

if __name__ == '__main__':
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        first, second = map(int, input().split())
        graph[first].append(second)

    solution(n, k, x, graph)