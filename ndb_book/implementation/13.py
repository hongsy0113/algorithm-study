import sys
from collections import deque
import heapq
from collections import defaultdict

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] 

def get_chicken_dist(x, y, graph, visited, chicken_dict):
    visited[x][y] = True
    queue = deque([(x, y, 0)])
    finish = None
    while queue:
        v_x, v_y, dist =  queue.popleft()
        for i in range(4):
            nx = v_x + dx[i]
            ny = v_y + dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if graph[nx][ny] == 2:
                    finish = True
                    chicken_dict[(nx, ny)] += dist + 1
                else:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
        if finish : return dist+1
    
# 각 치킨집만 있다고 가정했을 때의 치킨 거리 구하자
def get_distance (x, y, graph, visited):
    visited[x][y] = True
    total_dist = 0
    queue = deque([(x, y, 0)])

    while queue:
        v_x, v_y, dist = queue.popleft()

        for i in range(4):
            nx = v_x + dx[i]
            ny = v_y + dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph) and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    print(f'집 {nx}, {ny} 까지 거리는 {dist+1}')
                    total_dist += dist + 1         
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    

    return total_dist

def solution(n, m, graph):
    dist_per_chicken = []
    chicken_dict = defaultdict(int)
    # 각 치킨 집 마다 자신으로부터 모든 집까지의 거리 합을 구한다
    # for i in range(n):
    #     for j in range(n):
    #         if graph[i][j] == 2:
    #             print(f'치킨집 {i},{j}')
    #             visited = [[False] * n for _ in range(n)]
    #             dist = get_distance(i, j, graph, visited)
    #             print('total dist\n', dist)
    #             dist_per_chicken.append((-dist,i, j))
    # heapq.heapify(dist_per_chicken)
    # print(dist_per_chicken)

    # # TODO : 거리 값이 제일 큰 M개의 치킨집을 제거한다
    # remove_num = len(dist_per_chicken) - m
    # for _ in range(remove_num):
    #     dist, x,y = heapq.heappop(dist_per_chicken)
    #     graph[x][y] = 0
    # # 디버그 용
    # for i in range(n):
    #     print(graph[i])
    # # TODO: 제거 후 치킨 거리 구한다
    total_chicken_dist = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                visited = [[False] * n for _ in range(n)]
                get_chicken_dist(i, j, graph, visited, chicken_dict)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                dist_per_chicken.append((-chicken_dict[(i,j)] if chicken_dict[(i,j)]!=0 else -2*n, i, j))
    heapq.heapify(dist_per_chicken)
    print(dist_per_chicken)
    print(chicken_dict)
    # TODO : 거리 값이 제일 큰 M개의 치킨집을 제거한다
    remove_num = len(dist_per_chicken) - m
    for _ in range(remove_num):
        dist, x,y = heapq.heappop(dist_per_chicken)
        graph[x][y] = 0
    # 디버그 용
    for i in range(n):
        print(graph[i])
    # TODO: 제거 후 치킨 거리 구한다
    
    total_chicken_dist = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                visited = [[False] * n for _ in range(n)]
                total_chicken_dist+=get_chicken_dist(i, j, graph, visited, chicken_dict)
    print(total_chicken_dist)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    solution(n, m, graph)