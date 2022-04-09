from collections import deque
import sys
input = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs 함수
def bfs(start, graph, visited, m, n):
    visited[start[0]][start[1]] = True
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


# m: 가로길이, n: 세로길이
# graph: 배추는 1, 그 외 0인 2차원 m*n 리스트
def solution(m, n, graph):
    
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                # graph 탐색
                bfs((i,j), graph, visited, m, n)
                cnt += 1
                
    return cnt

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m, k = map(int, input().split())
        # graph 초기화
        graph = [[0] * n for _ in range(m)]
        for _ in range(k):
            y, x = map(int, input().split())
            graph[x][y] = 1
        print(solution(m, n, graph))
