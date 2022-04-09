import sys

def dfs(graph, com, visited, cnt):
    visited[com] = True
    cnt += 1

    for c in graph[com]:
        if not visited[c]:
            cnt = dfs(graph, c, visited, cnt)
    return cnt

def solution(n, graph):
    visited = [False] * (n+1)
    cnt = dfs(graph, 1, visited, 0)

    return cnt - 1

if __name__ == '__main__':
    n = int(input())
    e_cnt = int (input())
    graph = [[] for _ in range(n+1)]
    for _ in range(e_cnt):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(solution(n, graph))