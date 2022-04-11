from itertools import combinations
from collections import deque
import sys, copy

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS로 그래프에서 입력 바이러스 위치부터 시작해 바이러스를 전하
def bfs(start, graph, n, m):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 2

# 안전 영역의 크기 구함(빈 칸의 개수를 센다)
def get_safe_area(graph, n, m):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                bfs((i,j), graph, n, m)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

def print_graph(graph):
    for i in range(len(graph)):
        print(graph[i])

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    # 빈 칸의 좌표를 저장하는 리스트
    candidate = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 0:
                candidate.append((i, j))
        graph.append(row)
    
    max_cnt = 0 
    # combinations를 사용해 가능한 모든 조합으로 벽 설치
    for coord in  combinations(candidate, 3):
        temp_graph = copy.deepcopy(graph)
        for i in range(3):
            temp_graph[coord[i][0]][coord[i][1]] = 1
        new_cnt =  get_safe_area(temp_graph, n, m)
        if new_cnt > max_cnt:
            max_cnt = new_cnt
    print(max_cnt)
