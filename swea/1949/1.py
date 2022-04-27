import sys
sys.stdin = open("input.txt", "r")

# board를 벗어나는지 확인하는 함수
def in_board(r, c, N):
    if 0<=r<N and 0<=c<N:
        return True
    else:
        return False


# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#######
# 백트래킹에서 길이 업데이트용 전역변수 (초기화 필요)
length = 1
res = []
# 얘는 backtracking 호출될 때마다 값 정해지므로 초기화 필요 x
max_length = 1

# 시작 봉우리로부터 가장 긴 등산로 찾는 백트래킹 함수
# 함수의 모든 호출이 종료되면 전역변수 max_length에 최대 등산로 길이가 저장된다.
def backtracking(r, c):
    global length, max_length
    res.append((r,c))
    ### 이동 가능한 후보를 찾는다
    candidates = []
    height = board[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 자신보다 높은 낮은지 체크
        if in_board(nr, nc, N) and board[nr][nc] < height:
            candidates.append((nr, nc))

    ## candiate 없으면 종료
    if not candidates:
        max_length = max(length, max_length)
        return

    for candidate in candidates:
        length += 1
        backtracking(candidate[0], candidate[1])
        length -= 1




def len_init():
    global length, max_length
    length = 1
    max_length = 1

def soltuion(board, N, K, max_height):
    answer = 0
    ### TODO 0: 가장 높은 좌표 찾아서 리스트로 관리
    max_list = set([])
    for r in range(N):
        for c in range(N):
            if board[r][c] == max_height:
                max_list.add((r,c))


    # TODO 1 : 모든 경우에 대해서 깎아보고 최대 길이 등산로 구한다
    # 제일 먼저 아무것도 안 깎고 한 번 실행해서 max 값 갱신

    # 높은 봉우리마다 백트래킹
    for (r, c) in max_list:
        len_init()
        backtracking(r, c)
        answer = max(max_length, answer)

    ## k = 1 부터 K까지 반복
    for k in range(1, K+1):
        # 좌표 0번부터 N^2까지 반복
        for r in range(N):
            for c in range(N):
                # 해당 좌표를 k 만큼 깎는다.
                board[r][c] -= k
                # 제일 높은 봉우리를 깍은 경우 해당 봉우리는 탐색에서 제외
                if board[r][c] == max_height:
                    max_list.remove((r, c))
                # 제일 높은 봉우리에 대해서 반복
                for (start_r, start_c) in max_list:
                    # backtraking을 통해 가장 긴 등사로 길이 구한다
                    len_init()
                    backtracking(start_r, start_c)
                    # 최대값 갱신
                    ### debugging
                    if max_length > answer:
                        print(f'r, c : {start_r}, {start_c}  k : {k}, len : {max_length}')
                    answer = max(max_length, answer)
                # 깎은 거 원상복구
                board[r][c] += k
                board
                if board[r][c] == max_height:
                    max_list.add((r, c))

    return answer

if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        print(f'test case {test_case} start-------------------------------')
        N, K = map(int, input().split())
        board = []
        # 입력단계에서 제일 높은 값 기록
        max_height = 0
        for i in range(N):
            board.append(list(map(int, input().split())))
            max_height = max(max(board[i]), max_height)
        board
        print(soltuion(board, N, K, max_height))