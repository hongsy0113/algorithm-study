import sys
input = sys.stdin.readline

def search(x, y, graph, visited):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph) and not visited[nx][ny] and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            visited[nx][ny] = True            

# graph: 시험관 배열, virueses, 바이러스 종류 리스트
def solution(graph, n, viruses, S):
    for t in range(S):
        for virus in viruses:
            visited = [[False] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if graph[i][j] == virus and not visited[i][j]:
                        search(i, j, graph, visited)
    print_graph(graph)

def print_graph(graph):
    n = len(graph)
    for i in range(n):
        print(graph[i])

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    S, X, Y = map(int, input().split())

    viruses = [i for i in range(1, K+1)]

    solution(graph, N, viruses, S)
    print(graph[X-1][Y-1])