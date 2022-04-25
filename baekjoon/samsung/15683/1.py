import sys
input = sys.stdin.readline
import itertools
import copy

# 지도 출력하는 함수
def print_board(board):
    for i in range(len(board)):
        print(board[i])
    print()

# 특정 좌표가 지도를 넘어가지 않는지 확인하는 함수
def in_board(r, c, N, M):
    if 0<=r<N and 0<=c<M:
        return True
    else:
        return False

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 입력으로 상하좌우 중 한 방향을 받아 감시를 진행하는 함수
# 0: 상, 1: 우, 2: 하, 3: 좌
def _watch(board, r, c, direction, N, M):
    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]
        if in_board(nr, nc, N, M):
            # 다음 칸 벽이면 종료
            if board[nr][nc] == 6:
                break
            else:
                r = nr
                c = nc
                if board[nr][nc] == 0:
                    board[nr][nc] = -1
        # 지도 넘어가면 종료
        else:
            break

# cctv 정보를 바탕으로 감시 시작
# cctv가 상하좌우 중 어디 감사하게 되는지 구한다.
def watch(board, r, c, cctv, N, M):
    # cctv 정보를 배열로 관리
    # [cctv 번호, 90도로 몇번 회전했는지]
    cctv_type, cctv_rotate = cctv[0], cctv[1]
    # cctv 정보에 맞게 상하좌우 중 어느 방향을 감시하게 되는지를 directions 리스트에 저장
    if cctv_type == 1:
        # 1번 cctv의 경우 회전회수 + 1 이 방향임
        directions = [(cctv_rotate + 1) % 4]
    elif cctv_type == 2:
        # 회전 안 한 경우 0
        if cctv_rotate == 0:
            directions = [1, 3]
        else:
            directions = [0, 2]
    elif cctv_type == 3:
        if cctv_rotate == 0:
            directions = [0, 1]
        elif cctv_rotate == 1:
            directions = [1, 2]
        elif cctv_rotate == 2:
            directions = [2, 3]
        elif cctv_rotate == 3:
            directions = [3, 0]
    elif cctv_type == 4:
        if cctv_rotate == 0:
            directions = [0, 1, 3]
        elif cctv_rotate == 1:
            directions = [0, 1, 2]
        elif cctv_rotate == 2:
            directions = [1, 2, 3]
        elif cctv_rotate == 3:
            directions = [2, 3, 0]
    elif cctv_type == 5:
        directions = [0, 1, 2, 3]
    # directions 리스트에 있는 모든 방향에 대해서 감시 시작
    for direction in directions:
        _watch(board, r, c, direction, N, M)

# 사각지대가 총 몇칸인지 계산하는 함수
def get_unwatched(board):
    cnt = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                cnt += 1
    return cnt

def solution(board, N, M, candidates):
    min_cnt = 64
    # 모든 rotation 경우의 수에 대해서 탐색
    for candidate in candidates:
        # 각 경우는 독립적으로 시뮬레이션 되어야 하므로 deepcopy
        _board = copy.deepcopy((board))
        idx = 0
        for r in range(N):
            for c in range(M):
                if 1<=_board[r][c]<=5:
                    # 해당 cctv의 rotation을 어떻게 할지는 candidate를 찹고
                    watch(_board, r, c, [_board[r][c], candidate[idx]], N, M)
                    # candidate의 cctv 인덱스와 board에서 접근하는 cctv 순서가 같도록 증가
                    idx += 1
                    pass
        ## 사각지대 계산
        cnt = get_unwatched(_board)
        if cnt < min_cnt:
            min_cnt = cnt
    return min_cnt

# cctv 번호가 적힌 리스트를 입력으로 받는다
# 해당 리스트는 위에서 아래행, 왼쪽에서 오른쪽 순으로 탐색한 순서대로 cctv 번호가 들어가 있다.
# 가능한 모든 조합이 담긴 2차원 리스트를 반환하자
def get_cases(cctvs):
    n = len(cctvs)
    rotate_cases=[]
    for cctv in cctvs:
        if cctv in [1, 3, 4]:
            rotate_cases.append([0,1,2,3])
        elif cctv == 2:
            rotate_cases.append([0, 1])
        elif cctv == 5:
            rotate_cases.append([0])

    return list(itertools.product(*rotate_cases))


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    cctvs = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(M):
            ## CCTV이면 배열에 저장
            if 1<=board[i][j]<=5:
                cctvs.append(board[i][j])
    candidates = get_cases(cctvs)
    print(solution(board, N, M, candidates ))
