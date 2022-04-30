import sys
sys.stdin = open("big_input.txt", "r")
from collections import deque


def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 터널 타입을 key로 하고 연결된 방향 리스트를 value로 하는 dictionary 정의
tunnel_dict = {
    1 : [0, 1, 2, 3],
    2 : [0, 2],
    3 : [1, 3],
    4 : [0, 1],
    5 : [1, 2],
    6 : [2, 3],
    7 : [0, 3],
}

def bfs(board, r, c, L, visited):
    # queue에 좌표에 맨홀로부터 거리를 넣는다
    queue = deque([(r, c, 1)])
    visited[r][c] = True
    cnt = 1
    while queue:
        r, c, dist =queue.popleft()
        # L 시간이 지났으면 break
        if dist >= L: break

        tunnel_type = board[r][c]
        # 현재위치의 터널 종류를 보고 어느 방향으로 갈 수 있는지 확인
        for d in tunnel_dict[tunnel_type]:
            nr = r + dr[d]
            nc = c + dc[d]
            # 이동이 가능하려면 지도를 벗어나면 안 되고
            if not (0<=nr<N and 0<=nc<M):
                continue
            # 다음 위치에 있는 터널 타입이 잘 맞아야한다.
            # 즉 다음 위치에 있는 터널이 d의 역방향을 포함해야 한다
            # ex. 왼쪽으로 간거면 왼쪽 칸에 오른쪽으로 연결되는 터널 있어야 함

            # 먼저, 터널이 없거나 방문한 노드라면 continue
            if board[nr][nc] == 0 or visited[nr][nc]:
                continue
            next_tunnel_type = board[nr][nc]
            if (d+2) % 4 in tunnel_dict[next_tunnel_type]:
                queue.append((nr, nc, dist + 1))
                visited[nr][nc] = True
                cnt += 1

    return cnt


def solution(board, N, M, R, C, L):
    # TODO: bfs 함수로 탐색
    visited = [[False] * M for _ in range(N)]

    answer = bfs(board,  R, C, L, visited)

    return answer



if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N, M, R, C, L = map(int, input().split())
        board = []
        for i in range(N):
            board.append(list(map(int, input().split())))

        answer = solution(board, N, M, R, C, L)

        print(f'#{test_case} {answer}')