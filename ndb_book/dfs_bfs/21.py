# 시간초과
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


# L, R에 따라 국경을 여는 함수
# 인접리스트로 두 나라가 인접함을 표시
# 딕셔너리(인접리스트) 리턴
def open_border(land, N, L, R):
    adj_dict = defaultdict(list)
    # 모든 나라를 탐색
    # 각 나라 기준으로 자신의 오른쪽, 아래 나라만 비교한다
    dx = [0, 1]
    dy = [1, 0]
    for i in range(N):
        for j in range(N):
            for k in range(2):
                nx = i + dx[k]
                ny = j+dy[k]
                if not (0<=nx<N and 0<=ny<N): continue
                if L<= abs(land[i][j] - land[nx][ny]) <= R:
                    adj_dict[(i, j)].append((nx, ny))
                    adj_dict[(nx, ny)].append((i, j))

    return adj_dict

def bfs(x,y, land, N, visited, adj_dict):
    # 연합의 총 인구 , 연합 목록
    total_population = 0
    union_list = []
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        union_list.append((x,y))
        total_population += land[x][y]
        for (nx, ny) in adj_dict[(x,y)]:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                

    return total_population, union_list


def solution(land, N, L, R):
    time = 0
    while True:
        # 국경선 개방하는 과정. 개방 후 인접 리스트를 딕셔너리로 반환
        adj_dict = open_border(land, N, L, R)
        # 인접 리스트에 정보가 없다면 국경 개방이 없었다는 의미이므로 break
        if len(adj_dict) == 0:
            break
        # TODO: adj_dict로 연합 찾기
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    # TODO bfs/dfs 탐색
                    total_population, union_list = bfs(i, j, land, N, visited, adj_dict)
                    population = total_population // len(union_list)
                    for (x, y) in union_list:
                        land[x][y] = population
        time += 1
    return time

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    land = []

    for _ in range(N):
        land.append(list(map(int, input().split())))
    
    print(solution(land, N, L, R))