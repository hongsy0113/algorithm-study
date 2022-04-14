import sys
from collections import defaultdict, deque
input = sys.stdin.readline


# # L, R에 따라 국경을 여는 함수
# # 인접리스트로 두 나라가 인접함을 표시
# # 딕셔너리(인접리스트) 리턴
# def open_border(land, N, L, R):
#     adj_dict = defaultdict(list)
#     # 모든 나라를 탐색
#     # 각 나라 기준으로 자신의 오른쪽, 아래 나라만 비교한다
#     dx = [0, 1]
#     dy = [1, 0]
#     for i in range(N):
#         for j in range(N):
#             for k in range(2):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if not (0<=nx<N and 0<=ny<N): continue
#                 if L<= abs(land[i][j] - land[nx][ny]) <= R:
#                     adj_dict[(i, j)].append((nx, ny))
#                     adj_dict[(nx, ny)].append((i, j))

#     return adj_dict

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# bfs 함수에서 인구 차이를 비교하면서 탐색
def bfs(x,y, land, N, visited, L, R):
    # 연합의 총 인구 , 연합 목록
    total_population = 0
    union_list = []
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        union_list.append((x,y))
        total_population += land[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and L<=abs(land[x][y] - land[nx][ny])<=R:
                visited[nx][ny] = True
                queue.append((nx,ny))

    return total_population, union_list


def solution(land, N, L, R):
    time = 0
    
    while True:
        finished = True
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    # TODO bfs/dfs 탐색
                    total_population, union_list = bfs(i, j, land, N, visited, L, R)
                    population = total_population // len(union_list)
                    for (x, y) in union_list:
                        land[x][y] = population
                    # union_list에는 자기 자신이 들어감
                    # 길이가 2 이상이라면 연합이 생겨 인구이동이 있다는 뜻이므로 종료하면 안 됨.
                    if len(union_list) > 1:
                        finished = False
        if finished: break
        time+=1
    return time

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    land = []

    for _ in range(N):
        land.append(list(map(int, input().split())))
    
    print(solution(land, N, L, R))