import sys
input = sys.stdin.readline
from collections import deque

def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

# 좌표가 board을 벗어나는지 확인하는 함수
def in_board(r, c, N, M):
    if 0<r<=N and 0<c<=M:
        return True
    else:
        return False

## 점수 구하는 함수
# 동적프로그래밍을 이용해 한번 계산된 점수는 계산하지 않도록 한다
def get_score(r, c, board, score_dp):
    N = len(score_dp) - 1
    M = len(score_dp[0]) -1
    visited = [[False] * (M+1) for _ in range(N+1)]
    visited[r][c] = True
    # 같은 값 좌표를 저장하는 리스트
    _list = [(r,c)]
    value = board[r][c]
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        # 인접 노드 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_board(nr, nc, N, M) and not visited[nr][nc] and board[nr][nc] == value:
                queue.append((nr, nc))
                visited[nr][nc] = True
                _list.append((nr, nc))
    # 총 값이 같은 칸의 개수
    count = len(_list)
    for r, c in _list:
        score_dp[r][c] = value * count


# 북쪽 남쪽 이동을 위한 함수
# 동쪽 포인터는 변동 없으므로 다음 up포인트를 구한다
def get_next_up(up, east, direction):
    # east를 기준으로 up 위치가 어떻게 이동하는지 리스트로 저장
    if east == 1:
        arr = [2,4,5,3]
    elif east == 2:
        arr = [4,1,3,6]
    elif east == 3:
        arr = [2,1,5,6]
    elif east == 4:
        arr = [6,5,1,2]
    elif east == 5:
        arr = [6,3,1,4]
    elif east == 6:
        arr = [3,5,4,2]
    # 인덱스 상으로 북쪽이면 1 증가 ,남쪽이면 1 감소
    d = 1 if direction == 3 else -1
    idx = arr.index(up)
    next_up = arr[(idx + d) % 4]
    return next_up


# 주사위 이동 후 up, east 수정하는 함수
def move (r, c, board, d, up, east):
    nr = r + dr[d]
    nc = c + dc[d]
    # 동쪽인 경우
    if d == 0:
        west = 7 - east
        east = up
        up = west
    # 서쪽인 경우
    elif d == 2:
        down = 7 - up
        up = east
        east = down
    else:
        up = get_next_up(up, east, d)
    return nr, nc, up, east
# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution(board, N, M, K):
    total_score = 0
    r, c = 1, 1
    d = 0
    up = 1
    east = 3
    # 점수 저장하는 dp 테이블
    score_dp = [[0] * (M+1) for _ in range(N+1)]

    for k in range(K):
        # 1. 이동방향으로 한 칸 굴러갈 수 있는지 없는지 확인
        nr = r + dr[d]
        nc = c + dc[d]
        if in_board(nr, nc, N, M):
            # 가능하다면 굴러간다
            r, c, up, east = move(r, c, board, d, up, east)
        else:
            # 불가능하다면 뒤로 한칸 굴러간다
            d = (d-2)%4
            r, c, up, east = move(r, c, board, d, up, east)
        # 2. 점수를 획득한다
        # 점수획득하는 함수 호출(bfs/dfs)
        if score_dp[r][c] == 0:
            get_score(r, c, board, score_dp)

        score = score_dp[r][c]
        total_score += score

        # 3. 이동 방향 결정
        A = 7 - up
        B = board[r][c]
        if A > B:
            d = (d+1) % 4
        elif A < B:
            d = (d-1) % 4
        # print(f'좌표 ({r}, {c}), up:{up}, east:{east}, 방향: {d}')
    # print_board(score_dp)
    return total_score

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [[0]*(M+1)]
    for _ in range(N):
        board.append([0] + list(map(int, input().split())))

    print(solution(board, N,M, K))

