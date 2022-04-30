import sys
sys.stdin = open("big_input.txt", "r")
import time
start = time.time()

def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

## 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

class Ball:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.score = 0
        self.init_r = r
        self.init_c = c

    def move(self):
        nr = self.r + dr[self.d]
        nc = self.c + dc[self.d]


        # 블랙홀이거나 초기위치인 경우 False 리턴
        if 0<nr<=N and 0<nr<=N:
            if board[nr][nc] == -1 or (nr, nc) == (self.init_r, self.init_c):
                return False

        # 벽을 마주치거나 5번을 마주치는 경우
        if not(0<nr<=N and 0<nc<=N):
            ##방향만 반대로
            # but 위치도 임시적으로 이동했다고 치고 다시 돌아오자. 웜홀 나오자마자 벽인 경우 고려해서
            self.d = (self.d - 2) % 4
            # 점수 증가
            self.score += 1
            self.r = nr
            self.c = nc
        elif board[nr][nc] == 5:
            self.d = (self.d - 2) % 4
            # 점수 증가
            self.score += 1
            self.r = nr
            self.c = nc
        elif 1<=board[nr][nc]<=4:
            # 위치는 nr, nc로 바꾸고 방향은 경우에 따라 달라질 수도
            # 함수를 통해 다음 진행방향 구하자
            nd = self.get_next_direction(self.d, board[nr][nc])
            self.d = nd

            self.r = nr
            self.c = nc
            self.score += 1
        # 웜홀인 경우
        # 방향은 유지하고 위치만 바뀌는 게 포인트
        # 처음 입력에서 웝홀 위치 저장해 놓자
        elif 6<=board[nr][nc]<=10:
            hole_num = board[nr][nc]
            idx = wormhole_dict[hole_num].index((nr, nc))
            # idx 가 0이라면 idx = 1의 좌표가 다음 위치가 된다
            next_idx = (idx + 1) % 2
            self.r = wormhole_dict[hole_num][next_idx][0]
            self.c = wormhole_dict[hole_num][next_idx][1]
        # 그냥 일반적인 경우
        else:
            self.r = nr
            self.c = nc

        return True



    def get_next_direction(self, d, block_num):
        """

        :param d: 현재 이동중인 방향
        :param block_num: 맞닥뜨린 블록 종류
        :return: 새롭게 바뀐 이동 방향,
        """
        if block_num == 1:
            ## 우, 상 은 벽과 동일,
            if d == 0 or d == 1:
                d = (d + 2)
            elif d == 3:
                d = 0
            elif d == 2:
                d = 1
        elif block_num == 2:
            # 하, 우 는 벽과 동일
            if d == 1 or d == 2:
                d = (d + 2) % 4
            elif d == 0:
                d = 1
            elif d == 3:
                d = 2
        elif block_num == 3:
            # 하, 좌 는 벽과 동일
            if d == 2 or d == 3:
                d = d - 2
            elif d == 0:
                d = 3
            elif d == 1:
                d = 2
        elif block_num == 4:
            # 상, 좌는 벽과 동일
            if d == 0 or d == 3:
                d = (d + 2) % 4
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3

        return d

    def __str__(self):
        return f"위치 ({self.r}, {self.c}), 방향 {self.d}"





def solution(board, N):

    ## TODO 모든 좌표에 대해서 모든 방향에 대해서 시뮬레이션
    max_score = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            # 블록, 웜홀 또는 블랙홀이 있는 위치에서는 출발할 수 없다.
            if board[r][c] == 0:
                for d in range(4):
                    ball = Ball(r, c, d)
                    # todo 종료 조건 될 때까지 시뮬레이션
                    while True:
                        if ball.move() == False:
                            max_score = max(ball.score, max_score)
                            break

    return max_score
    # 점수 카운트


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        ### 상하좌우 한칸씩 추가공간 놓자
        board = [[0] * (N+2)]
        wormhole_dict = {}
        for i in range(1, N+1):
            board.append([0] + list(map(int, input().split())) + [0])
            for j in range(1, N+1):
                if 6<= board[i][j]<= 10:
                    if not board[i][j] in wormhole_dict:
                        wormhole_dict[board[i][j]] = [(i, j)]
                    else:
                        wormhole_dict[board[i][j]].append((i, j))
        board.append([0] * (N+2))
        answer = solution(board, N)
        print(f'#{test_case} {answer}')


print('time: ', time.time() - start )