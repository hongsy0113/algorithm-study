import sys
input = sys.stdin.readline

def search_by_row(N, L, board):
    count = 0
    # 행을 따라서 탐색 (가로길)
    for r in range(N):
        # 경사로의 방향도 중요하다
        down_slope = []
        flag = True
        # 이전 칸의 높이와 현재 칸의 높이를 비교하기 위해 1부터 시작
        # 같은 높이가 얼머나 연속되었는지 카운트
        for c in range(1, N):

            # 높이가 같으면 skip
            if board[r][c] == board[r][c - 1]:
                continue
            # 높이가 낮아진 경우
            elif board[r][c] < board[r][c - 1]:
                cur_count = 1
                temp = board[r][c]
                # 낮은 높이가 L개 연속되어 있는지 확인
                for i in range(1, L):
                    if c + i < N and board[r][c + i] == temp:
                        cur_count += 1
                    else:
                        # 실패하는 경우
                        break
                # 경사로 놓은 것은 리스트에 열번호를 넣어서 관리
                if cur_count >= L:
                    for i in range(L):
                        down_slope.append(c + i)
                # 경사로 놓는 것이 불가능하면 해당 길은 이동 불가능
                else:
                    flag = False
                    break
            # 높이가 높아지는 경우
            else:
                temp = board[r][c-1]

                cur_count = 0
                # L개 이상 연속됐어서 설치 가능한 경우
                for i in range(1, L+2):
                    if c - i >= 0  and board[r][c - i] == temp and not c-i in down_slope:
                        cur_count += 1
                    else:
                        # 실패하는 경우
                        break
                if cur_count < L:
                    flag = False
                    break
        if flag: count += 1
    return count

def search_by_col(N, L, board):
    count = 0
    # 열을 따라서 탐색 (세로길)
    for c in range(N):
        # 경사로의 방향도 중요하다
        down_slope = []
        flag = True
        # 이전 칸의 높이와 현재 칸의 높이를 비교하기 위해 1부터 시작
        # 같은 높이가 얼머나 연속되었는지 카운트
        for r in range(1, N):

            # 높이가 같으면 skip
            if board[r][c] == board[r - 1][c]:
                continue
            # 높이가 낮아진 경우
            elif board[r][c] < board[r - 1][c]:
                cur_count = 1
                temp = board[r][c]
                # 낮은 높이가 L개 연속되어 있는지 확인
                for i in range(1, L):
                    if r + i < N and board[r + i][c] == temp:
                        cur_count += 1
                    else:
                        # 실패하는 경우
                        break
                # 경사로 놓은 것은 리스트에 열번호를 넣어서 관리
                if cur_count >= L:
                    for i in range(L):
                        down_slope.append(r + i)
                # 경사로 놓는 것이 불가능하면 해당 길은 이동 불가능
                else:
                    flag = False
                    break
            # 높이가 높아지는 경우
            else:
                temp = board[r - 1][c]

                cur_count = 0
                # L개 이상 연속됐어서 설치 가능한 경우
                for i in range(1, L+2):
                    if r - i >= 0  and board[r - i][c] == temp and not r-i in down_slope:
                        cur_count += 1
                    else:
                        # 실패하는 경우
                        break
                if cur_count < L:
                    flag = False
                    break
        if flag: count += 1
    return count


def solution(N, L, board):
    count = search_by_row(N, L, board) + search_by_col(N, L, board)
    return count

if __name__ == '__main__':
    N, L = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = solution(N, L, board)
    print(answer)
