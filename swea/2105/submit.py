import sys
sys.stdin = open("input.txt", "r")

## 우하,좌하, 좌상, 우상 순
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]



def init(r, c):
    global res, start, disert_sum
    disert_sum = 0
    start = (r, c)
    res = set([board[r][c]])
    disert_sum = 0

## 백트래킹용 변수들
disert_sum = 0

def backtracking(r, c, d):
    global disert_sum, answer
    ## 다시 되돌아 오면 종료조건
    if d == 3 and (r, c) == start:
        answer = max(len(res), answer)
        return


    # 방향을 탐색 해봄
    # 현재 방향 그대로
    # or 시계방향으로 꺾어서

    # 기존에 없던 값이라면 res에 넣고, r, c 갱신하고 재귀 함수 호출
    # 호출문 끝나고 res 에서 값 뺀다.
    # 누적합 값 계산해도 괜찮을 듯

    # 방향 꺾었던 경우에는 호출 완료 후 방향 원래대로

    # 1. 현재 방향 그대로
    nr = r + dr[d]
    nc = c + dc[d]
    # board 벗어나면 안 됨
    if (0<=nr<N and 0<=nc<N) and not board[nr][nc] in res:
        res.add(board[nr][nc])
        backtracking(nr, nc, d)
        res.remove(board[nr][nc])

    ###
    # 다음 이동칸이 start라면
    if (nr, nc) == start:
        backtracking(nr, nc, d)


    ## 아직 첫 시작이면 방향 꺽으면 안 됨
    if len(res) > 1:

        ## 2. 방향 꺽어서
        nd = (d + 1) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        # board 벗어나면 return
        if (0<=nr<N and 0<=nc<N) and not board[nr][nc] in res:

            res.add(board[nr][nc])
            backtracking(nr, nc, nd)
            res.remove(board[nr][nc])

        # 다음 이동칸이 start라면
        if (nr, nc) == start:
            backtracking(nr, nc, nd)



def solution(board, N):

    init(0, 2)
    backtracking(0, 2, 0)

    for r in range(N-2):
        for c in range(1, N-1):
            init(r, c)
            backtracking(r, c, 0)




if __name__ == '__main__':

    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        board = []
        for _ in range(N):
            board.append(list(map(int, input().split())))
        answer = -1
        solution(board, N)
        print(f'#{test_case} {answer}')