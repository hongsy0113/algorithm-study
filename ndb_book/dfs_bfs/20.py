import sys
from itertools import combinations
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def _search(x, y, graph):
    # 각 방향으로 끝까지 쭉 확인해보면 됨
    for i in range(4):
        can_find = False
        nx, ny = x, y
        # 해당 방향으로 가능할 때까지 탐색
        # 벽에 닿거나, 장애물에 닿으면 탐색 종료, S에 닿으면 True를 리턴후 종료
        while True:
            nx = nx + dx[i]
            ny = ny + dy[i]
            if not(0<=nx<len(graph) and 0<=ny<len(graph)):
                break
            if graph[nx][ny] == 'W':
                break
            if graph[nx][ny] == 'S':
                can_find = True
                break
        # 학생을 한 명이라도 발견했다면 추가 탐색 없이 False 리턴
        if can_find == True:
            return False
    return True

# 해당 그래프에서 학생들이 감시에 피해지는지 확인
# 선생님을 기준으로 상하좌우 탐색을 실행한다
def search(graph, n):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T' and not visited[i][j]:
                # 탐색 실행하고 감시 피하기가 실패라면 바로 false 리턴
                if _search(i, j, graph) == False:
                    return False
    return True
    
# 입력 데이터를 통해 벽 3개로 모든 학생 감시 피할 수 있다면 'YES' 아니면 'NO' 리턴
def solution(graph, n, candidates):
    it = combinations(candidates, 3)
    # 모든 벽 조합을 다 고려
    for walls in it:
        temp_graph = copy.deepcopy(graph)
        for wall in walls:
            temp_graph[wall[0]][wall[1]] = 'W'
        ## TODO : 벽 세개를 세우고 탐색
        # 해당 벽 조합으로 감시 피하기가 가능했다면 바로 'YES' 리턴
        if search(temp_graph, len(graph)) == True:
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    N = int(input())
    # 그래프를 입력 받으면서 빈칸의 위치 좌표도 리스트에 담아놓는다
    blank_list = []
    graph = []
    for i in range(N):
        row = list(input().split())
        for j in range(N):
            if row[j] == 'X':
                blank_list.append((i,j))
        graph.append(row)
    
    answer = solution(graph, N, blank_list)
    print(answer)