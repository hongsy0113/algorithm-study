import sys
from collections import deque
input = sys.stdin.readline

def search(graph, queue):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    pos_list = []    
    while queue:
        pos_list.append(queue.popleft())
    for (x, y) in pos_list:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph) and  graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny))

# graph: 시험관 배열, virueses, 바이러스 종류 리스트
def solution(graph, n, viruses, S):
    for t in range(S):
        for virus, poses in viruses.items():
            search(graph, poses)
    print_graph(graph)

def print_graph(graph):
    n = len(graph)
    for i in range(n):
        print(graph[i])

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = []
    # virus가 나오면 dict에 저장
    virus_dict = {}
    for i in range(N):
        graph.append(list(map(int, input().split())))
        for j in range(N):
            if graph[i][j] != 0:
                if graph[i][j] in virus_dict:
                    virus_dict[graph[i][j]].append((i, j))
                else:
                    virus_dict[graph[i][j]] = deque([(i, j)])
    S, X, Y = map(int, input().split())

    # 바이러스 딕셔너리 정렬
    virus_dict = sorted(virus_dict.items())
    virus_dict=  dict(virus_dict)
    solution(graph, N, virus_dict, S)
    print(graph[X-1][Y-1])