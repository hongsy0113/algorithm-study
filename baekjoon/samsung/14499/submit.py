import sys
input = sys.stdin.readline

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 주사위 전개도상에서 반대편 면의 번호를 반환하는 함수
def get_opposite(side):
    return 7 - side

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
    # 인덱스 상으로 남쪽이면 1 감소, 북쪽이면 1 증가
    d = 1 if direction == 3 else -1
    idx = arr.index(up)
    next_up = arr[(idx + d) % 4]
    return next_up

# 이동 후 새로운 주사위 좌표 반환
def move (n, m, x, y, board, direction, dice, up, east):
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 지도의 바깥인지 확인
    if not(0<=nx<n and 0<=ny<m):
        return x, y, up, east
    # up 포인터와 east 포인터를 수정
    if direction == 1:
        west = get_opposite(east)
        east = up
        up = west
    elif direction == 2:
        down = get_opposite(up)
        up = east
        east = down

    else:
        up = get_next_up(up,east,direction)

    # TODO : 값 수정하는 로직
    if board[nx][ny] == 0:
        board[nx][ny] = dice[get_opposite(up)]
    else:
        dice[get_opposite(up)] = board[nx][ny]
        board[nx][ny] = 0
    # 상단 값 출력
    print(dice[up])

    return nx, ny, up, east


def solution(N, M, x, y, K, board, commands):
    # 다이스를 0으로 초기화
    # 문제에서의 전개도를 기반으로 하고 해당 전개도의 위치의 있는 값을 알기 위해서 dict[인덱스]로 접근
    dice = [0] * 7
    # 값은 dice 리스트로 관리, dice의 놓인 위치 및 방향은 up, east 포인터 두개로 관리
    up, east = 1, 3
    for command in commands:
        # TODO
        # command에 따라 움직인다
        x, y, up, east = move(N, M, x, y, board, command, dice, up, east)

if __name__ == '__main__':
    N, M, x, y, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    commands = list(map(int, input().split()))

    solution(N, M, x, y, K, board, commands)