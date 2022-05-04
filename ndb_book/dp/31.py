
def solution(board, m, n):
    # 2차원 dp 테이블 정의
    dp = [[0] * m for _ in range(n)]

    # 첫 열에 대한 dp 정보 채운다
    for r in range(n):
        dp[r][0] = board[r][0]

    # 한 열씩 dp 테이블 채워나간다
    # 점화식
    # dp[r][c] = board[r][c] + max(이전 열에서 선택할 수 있는 값들)
    for c in range(1, m):
        for r in range(n):
            candidates = []
            for i in range(-1, 2, 1):
                # 왼쪽 위, 왼쪽 아래, 왼쪽 중 유효한 경우를 candidates에 추가
                if 0<=r + i<n:
                    candidates.append(dp[r+i][c-1])
            dp[r][c] = board[r][c] + max(candidates)

    print(dp)
    print(max([row[-1] for row in dp]))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        board = [[0] * m for _ in range(n)]

        arr = list(map(int, input().split()))

        for i in range(len(arr)):
            r = i // 4
            c = i % 4
            board[r][c] = arr[i]
        solution(board, m, n)