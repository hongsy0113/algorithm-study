import sys
from collections import deque
from copy import deepcopy
from itertools import permutations
input = sys.stdin.readline

def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

def get_max_value(board):
    n = len(board)
    max_value = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > max_value:
                max_value = board[i][j]
    return max_value

# 블록을 이동시키는 함수
# direction 0 -> 상, 1-> 하, 2-> 좌, 3->우
def move(board, direction):
    n = len(board)
    changed_block = set([])
    # 위로 이동
    if direction == 0:
        # 2번째 행부터 이동
        for r in range(1, n):
            for c in range(n):
                # 빈칸이라면 skip
                if board[r][c] == 0:
                    continue
                # 한 칸씩 이동해본다. 최대 r 칸
                for k in range(1, r+1):
                    # k가 r인경우도 고려
                    if k == r:
                        if board[0][c] == 0:
                            # 블록이 이동
                            board[0][c] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                    # 빈칸이라면 계속 이동 가능하다
                    if board[r-k][c] == 0:
                        continue
                    # 자신과 같은 값이고 해당 블록이 합쳐진 블록이 아니라면
                    if board[r-k][c] == board[r][c] and not (r-k, c) in changed_block:
                        # 기존 위치는 0이 되고
                        board[r][c] = 0
                        # 새롭게 값이 합쳐짐
                        board[r-k][c] *= 2
                        # 해당 블록은 이미 합쳐진 값임을 알기 위해
                        changed_block.add((r-k, c))
                        break
                    # 자신과 다른 값을 만나거나 합쳐진 블록이라면
                    else:
                        # 블록이 이동
                        if k > 1:
                            # k 칸을 이동하려고 했지만 막힌 상황이므로 그 전 step 까지만
                            board[r-k+1][c] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                        # 한 칸도 이동 못하는 경우 .. 아무 변화 없어야 한다
                        else:
                            break
    # 아래로 이동
    elif direction == 1:
        # 마지막에서 2번째 행부터 이동
        for r in range(n-2, -1, -1):
            for c in range(n):
                # 빈칸이라면 skip
                if board[r][c] == 0:
                    continue
                # 한 칸씩 이동해본다. 최대 N - r - 1 칸
                for k in range(1, n - r):
                    # k가 N-r-1인경우도 고려
                    if k == n-r-1:
                        if board[n-1][c] == 0:
                            # 블록이 이동
                            board[n-1][c] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                    # 빈칸이라면 계속 이동 가능하다
                    if board[r+k][c] == 0:
                        continue
                    # 자신과 같은 값이고 해당 블록이 합쳐진 블록이 아니라면
                    if board[r+k][c] == board[r][c] and not (r+k, c) in changed_block:
                        # 기존 위치는 0이 되고
                        board[r][c] = 0
                        # 새롭게 값이 합쳐짐
                        board[r+k][c] *= 2
                        # 해당 블록은 이미 합쳐진 값임을 알기 위해
                        changed_block.add((r+k, c))
                        break
                    # 자신과 다른 값을 만나거나 합쳐진 블록이라면
                    else:
                        # 블록이 이동
                        if k > 1:
                            # k 칸을 이동하려고 했지만 막힌 상황이므로 그 전 step 까지만
                            board[r+k-1][c] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                        # 한 칸도 이동 못하는 경우 .. 아무 변화 없어야 한다
                        else:
                            break
    # 좌로 이동
    elif direction == 2:
        # 2번째 열부터 이동
        for c in range(1, n):
            for r in range(n):
                # 빈칸이라면 skip
                if board[r][c] == 0:
                    continue
                # 한 칸씩 이동해본다. 최대 c 칸
                for k in range(1, c + 1):
                    # k가 c인경우도 고려
                    if k == c:
                        if board[r][0] == 0:
                            # 블록이 이동
                            board[r][0] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                    # 빈칸이라면 계속 이동 가능하다
                    if board[r][c - k] == 0:
                        continue
                    # 자신과 같은 값이고 해당 블록이 합쳐진 블록이 아니라면
                    if board[r][c - k] == board[r][c] and not (r, c- k) in changed_block:
                        # 기존 위치는 0이 되고
                        board[r][c] = 0
                        # 새롭게 값이 합쳐짐
                        board[r][c - k] *= 2
                        # 해당 블록은 이미 합쳐진 값임을 알기 위해
                        changed_block.add((r, c - k))
                        break
                    # 자신과 다른 값을 만나거나 합쳐진 블록이라면
                    else:
                        # 블록이 이동
                        if k > 1:
                            # k 칸을 이동하려고 했지만 막힌 상황이므로 그 전 step 까지만
                            board[r][c - k + 1] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                        # 한 칸도 이동 못하는 경우 .. 아무 변화 없어야 한다
                        else:
                            break
    # 우로 이동
    elif direction == 3:
        # 마지막에서 2번째 열부터 이동
        for c in range(n-2, -1, -1):
            for r in range(n):
                # 빈칸이라면 skip
                if board[r][c] == 0:
                    continue
                # 한 칸씩 이동해본다. 최대 n - c - 1 칸
                for k in range(1, n - c):
                    # k가 n- c - 1인경우도 고려
                    if k == n- c - 1:
                        if board[r][n-1] == 0:
                            # 블록이 이동
                            board[r][n-1] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                    # 빈칸이라면 계속 이동 가능하다
                    if board[r][c + k] == 0:
                        continue
                    # 자신과 같은 값이고 해당 블록이 합쳐진 블록이 아니라면
                    if board[r][c + k] == board[r][c] and not (r, c + k) in changed_block:
                        # 기존 위치는 0이 되고
                        board[r][c] = 0
                        # 새롭게 값이 합쳐짐
                        board[r][c + k] *= 2
                        # 해당 블록은 이미 합쳐진 값임을 알기 위해
                        changed_block.add((r, c + k))
                        break
                    # 자신과 다른 값을 만나거나 합쳐진 블록이라면
                    else:
                        # 블록이 이동
                        if k > 1:
                            # k 칸을 이동하려고 했지만 막힌 상황이므로 그 전 step 까지만
                            board[r][c + k - 1] = board[r][c]
                            # 기존 위치는 0이 된다
                            board[r][c] = 0
                            break
                        # 한 칸도 이동 못하는 경우 .. 아무 변화 없어야 한다
                        else:
                            break

    return board

def solution(board):
    queue = deque([(board, 0)])
    max_value = 0
    while queue:
        board, step = queue.popleft()
        value = get_max_value(board)
        if step <= 5 and value > max_value:
            max_value = value
        if step > 5:
            break
        for i in range(4):
            new_board = deepcopy(board)
            new_board = move(new_board, i)
            queue.append((new_board, step+1))

    return max_value



if __name__ == '__main__':
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    if N == 1:
        answer = board[0][0]
    print(solution(board))
