import sys
input = sys.stdin.readline

# 해당 위치에서 모든 경우의 수 고려한 뒤 합의 최대값 리턴
def get_max_value(board, r, c, n, m):
    max_value = 0
    # 아래로 4칸 이상 여유 있는 경우
    if n - r >= 4:
        # 긴 블록
        value = sum([board[i][c] for i in range(r, r+4)])
        max_value = max(value, max_value)
    # 아래로 3칸 이상 여유 있는 경우
    if n - r >= 3 and m - c >= 2:
        ### (r,c) 기준으로 아래로 세칸까지 합 구한다
        value = sum([board[i][c] for i in range(r, r+3)])
        # 우측에 제일 큰 값 더한다
        value += max(board[r][c+1], board[r+1][c+1], board[r+2][c+1])
        max_value = max(value, max_value)

        ### (r, c+1) 기준으로 아래로 세칸까지 합 구한다
        value = sum([board[i][c+1] for i in range(r, r + 3)])
        # 좌측에 제일 큰 값 더한다
        value += max(board[r][c], board[r + 1][c], board[r + 2][c])
        max_value = max(value, max_value)

        ### ㄹ 같이 생긴 블록들 고려 (세로 모양일때)
        # 가운데 두 칸은 공통이므로 계산
        value = board[r+1][c] + board[r+1][c+1]
        value += max(board[r][c+1] + board[r+2][c], board[r][c] + board[r+2][c+1])
        max_value = max(value, max_value)
    # 아래로 두칸 이상 여유 있는 경우
    if n - r >= 2 and m - c >= 2:
        # 2x2 정사각형 고려
        value = board[r][c] + board[r+1][c] + board[r][c+1] + board[r+1][c+1]
        max_value = max(value, max_value)
        # 그 외 경우 고려
        if m - c >= 3:
            # (r, c) 기준으로 오른쪽으로 세칸까지 합 구한다
            value = sum([board[r][i] for i in range(c, c + 3)])
            # 아래 세칸 중 제일 큰 값 더한다
            value += max(board[r+1][c], board[r+1][c+1], board[r+1][c+2])
            max_value = max(value, max_value)

            # (r+1, c) 기준으로 오른쪽으로 세칸까지 합 구한다
            value = sum([board[r+1][i] for i in range(c, c + 3)])
            # 위 세칸 중 제일 큰 값 더한다
            value += max(board[r][c], board[r][c + 1], board[r][c + 2])
            max_value = max(value, max_value)

            # ㄹ 같이 생긴 블록들 고려(가로 모양일 때)
            # 가운데 두 칸은 공통이므로 먼저 계산
            value = board[r][c+1] + board[r+1][c+1]
            value += max(board[r][c] + board[r+1][c+2], board[r+1][c] + board[r][c+2])
            max_value = max(value, max_value)
    # 행 한 칸 여유있는 경우는 항상 그렇다고 가정
    if m - c >= 4:
        value = sum([board[r][i] for i in range(c, c+4)])
        max_value = max(value, max_value)

    return max_value

def solution(board, n, m):
    answer = 0
    for r in range(n):
        for c in range(m):
            value = get_max_value(board, r, c, n, m)
            if value > answer:
                answer = value

    return answer
if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    answer = solution(board, N, M)
    print(answer)