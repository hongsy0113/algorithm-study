import sys
input = sys.stdin.readline

INF = int(1e9)

def print_graph(graph):
    n = len(graph)
    for i in range(1, n):
        print(graph[i][1:])
    print()

def solution(graph, n):
    for i in range(1, n+1):
        graph[i][i] = 0
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if a != b:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

def print_answer(graph):
    n = len(graph) - 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            v = graph[i][j] if graph[i][j] != INF else 0
            print(v, end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
    solution(graph, n)
    print_answer(graph)