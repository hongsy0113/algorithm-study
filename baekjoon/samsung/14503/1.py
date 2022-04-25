import sys
input = sys.stdin.readline

# 북 동 남 서
# 인덱스 증가하면 오른쪽회전, 감소하면 왼쪽 회전
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(N, M, r, c, d, board):
    answer = 0
    while True:
        cnt_2a = 0
        # TODO : 1. 현재 위치를 청소한다.
        board[r][c] = 2
        answer += 1
        while True:
            # TODO: 2-b
            # 네 방향 모두 청소했는지 확인
            if cnt_2a >= 4:
                nr = r + dr[(d - 2) % 4]
                nc = c + dc[(d - 2) % 4]
                # 뒤에가 벽이라면 종료
                if board[nr][nc] == 1:
                    return answer
                # 방향을 유지한 채 뒤로 이동
                else:
                    r = nr
                    c = nc
                    cnt_2a = 0
            # TODO : 2-a.
            # 왼쪽 칸 확인
            nr = r + dr[(d-1) % 4]
            nc = c + dc[(d-1) % 4]
            # 왼쪽이 청소하지 않은 경우
            if board[nr][nc] == 0:
                d = (d-1) % 4
                r = nr
                c = nc
                break
            else:
                d = (d-1) % 4
                cnt_2a += 1
                continue

if __name__ == '__main__':
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    print(solution(N, M, r, c, d, board))