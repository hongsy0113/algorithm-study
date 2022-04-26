import sys
input = sys.stdin.readline
import copy

def print_board(board):
    n = len(board)
    for i in range(0, n):
        print(board[i][1:])
    print()

# 방향을 위한 배열
# idx 0부터 차례로 남서,  서, 북서, 북, 북동, 동, 남동, 남,
dr = [1, 0, -1, -1, -1, 0, 1, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0]

# board = [
#     [],
#     [{}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}],
#     [{}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}],
#     [{}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}],
#     [{}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}, {'shark':[], 'smell':[], 'fish':[]}],
# ]
board = [
    [],
    [{}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}],
    [{}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}],
    [{}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}],
    [{}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}, {'shark':0, 'smell':0, 'fish':0}],
]

# 각 좌표에 들어가 있는 fish 객체 저장
fish_board = [
    [[]],
    [[], [], [], [], []],
    [[], [], [], [], []],
    [[], [], [], [], []],
    [[], [], [], [], []],
    [[], [], [], [], []]
]


# 물고기부터 확실히 하자
class Fish:

    def __init__(self, r, c, direction):
        self.r = r
        self.c = c
        self.direction = direction

    def move(self):
        rotate_cnt = 0
        temp_direction = self.direction
        moved = False
        while rotate_cnt <=8:
            nr = self.r + dr[self.direction]
            nc = self.c + dc[self.direction]
            # 상어가 있는지, 물고기의 냄새가 있는지, 벗어나는지
            if 0<nr<=4 and 0<nc<=4 and board[nr][nc]['shark'] <= 0 and board[nr][nc]['smell'] <= 0:
                self.r = nr
                self.c = nc
                ## 움직였는지 여부를 return하고 그 값을 바탕으로 메인 루틴에서 fish를 삭제하고 삽입
                moved = True
                break
            # 불가능하다면 반시계 45도 회전
            else:
                self.direction = (self.direction-1) % 8
                rotate_cnt += 1
        # 안 움직이는 경우 원래 방향 유지
        if moved == False:
            self.direction = temp_direction
        return moved

    def __str__(self):
        return f"(r, c) : ({self.r}, {self.c}). 방향 {self.direction}"

class Smell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.life = 3

    # 수명을 감소시키고 수명이 0이되면 false 리턴턴
    def dec_life(self):
        self.life -= 1
        if self.life == 0:
            return False
        return True


class Shark:
    def __init__(self, r, c, s):
        self.r = r
        self.c = c
        self.s = s

    # TODO move 함수 작성하자
    def move(self):
        # board에서 shark 제거
        board[self.r][self.c]['shark'] = 0
        step, _ = self.get_best_case()
        for i in range(3):
            nr, nc, _ = self.test_move(self.r, self.c, str(step)[i])
            # 물고기 제외
            if board[nr][nc]['fish'] > 0:
                fish_board[nr][nc] = []
                board[nr][nc]['fish'] = 0
                # 냄새 생성하고 위치시키기
                smell = Smell(nr, nc)
                board[nr][nc]['smell'] += 1
                smell_list.append(smell)

            self.r = nr
            self.c = nc
        # board에서 shark 추가
        board[self.r][self.c]['shark'] = 1
    # 각 단계에서 상어가 움직일 세 칸 방향 구하는 함수
    def get_best_case(self):
        iterable = ['1', '2', '3', '4']
        candidate = []
        # 반복문을 돌면서 candidate에 가능한 모든 경우의 수를 넣는다. (세자리 자연수, 먹은 물고기수)
        for way1 in ['1', '2', '3', '4']:
            for way2 in ['1', '2', '3', '4']:
                for way3 in ['1', '2', '3', '4']:
                    cnt = 0

                    r, c = self.r, self.c
                    visited = set([(r, c)])
                    ###############1.
                    r, c, temp = self.test_move(r, c, way1)

                    # 격자를 벗어나는 것이므로 break
                    if temp == -1:
                        continue
                    else:
                        if not (r,c) in visited:
                            cnt += temp
                        visited.add((r, c))
                    ###############2.

                    r, c, temp = self.test_move(r, c, way2)
                    ###
                    # 격자를 벗어나는 것이므로 break
                    if temp == -1:
                        continue
                    else:
                        if not (r, c) in visited:
                            cnt += temp
                        visited.add((r, c))

                    ###############3.
                    r, c, temp = self.test_move(r, c, way3)

                    # 격자를 벗어나는 것이므로 break
                    if temp == -1:
                        continue
                    else:
                        if not (r, c) in visited:
                            cnt += temp
                        visited.add((r, c))

                    candidate.append((int(''.join([way1, way2, way3])), cnt))
        # candidate를 정렬
        candidate.sort(key= lambda x :( -x[1], x[0]))
        print(candidate)
        print(candidate[0])
        return candidate[0]

    # 상어가 가장 물고기 많이 먹을 수 있는 경로를 찾기 위해 한 칸 시뮬레이션 해보는 함수
    def test_move(self, r, c, way):
        # way는 상하좌우
        # direction 은 fish 와 같은 dr, dc 리스트 사용하기 위해 사용
        # 상은 북
        if way == '1':
            direction = 3
        # 좌는 서
        elif way == '2':
            direction = 1
        # 하는 남
        elif way == '3':
            direction = 7
        # 우는 동
        elif way == '4':
            direction = 5
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 이동 후 좌표와 먹은 물고기 수 반환
        # 격자를 넘어선다면 -1 반환
        if 0<nr<=4 and 0<nc<=4:
            cnt = board[nr][nc]['fish']
        else:
            cnt = -1
        return nr, nc, cnt

def get_fish_cnt(board):
    total_cnt = 0
    for r in range(1,5):
        for c in range(1,5):
            total_cnt += board[r][c]['fish']
    return total_cnt

if __name__ == '__main__':
    ## TODO: 입력 받기
    M, S = map(int,input().split())
    fish_list = []
    smell_list = []
    for _ in range(M):
        fx, fy, d = map(int,input().split())
        # fish 객체 생성 후 board에 추가
        fish = Fish(fx, fy, d)
        board[fx][fy]['fish'] += 1
        fish_list.append(fish)
    sx, sy = map(int, input().split())
    # TODO: 상어 객체 생성 후 board에 추가하기
    shark = Shark(sx, sy, S)
    board[sx][sy]['shark'] = 1

    ############
    ## S 번 반복
    for _ in range(S):

        ### 1. 상어가 복제마법 시전
        ## fish_list를 deepcopy해서 저장해놓자
        copyed_fish_list = copy.deepcopy(fish_list)
        ### 2. 모든 물고기 이동
        ## fish_list를 for문 돌려서 이동
        for fish in fish_list:
            # 기존 정보 저장용
            r = fish.r
            c = fish.c
            d = fish.direction
            # 움직였다면 board count 값 바꿔줌
            if fish.move():
                # fish_board도 수정
                for _fish in fish_board[r][c]:
                    if _fish.direction == d:
                        fish_board[r][c].remove(_fish)
                        break
                fish_board[fish.r][fish.c].append(fish)

                board[r][c]['fish'] -= 1
                board[fish.r][fish.c]['fish'] += 1
        ####
        print('상어이동전, 물고기 이동후')
        print_board(board)
        ### 3. 상어 이동
        ## shark.move로 이동
        ## 물고기 제거하는 부분 고민
        shark.move()

        ### 4. 냄새
        ## 냄새 수명 감소시키고 0 되는 냄새 있다면 board에서 제거
        for smell in smell_list:
            # 0 이 되면 false 반환
            if smell.dec_life() == False:
                board[smell.r][smell.c]['smell'] = 0
                smell_list.remove(smell)

        ### 5. 복제
        ## deepcopy 해두었던 fish_list를 반복시키면서 board에 count 증가시키고
        ## 기존 fish_list랑 합친다.
        for fish in copyed_fish_list:
            board[fish.r][fish.c]['fish'] += 1

            fish_board[fish.r][fish.c].append(fish)
        # fish_list를 새롭게 갱신
        fish_list = []
        for r in range(1,5):
            for c in range(1,5):
                fish_list = fish_list + fish_board[r][c]
        ####
        print_board(board)
    print(get_fish_cnt(board))

    ############



    # # TEST fish 이동
    # for fish in fish_list:
    #     r = fish.r
    #     c = fish.c
    #     # 움직였다면 board count 값 바꿔줌
    #     if fish.move():
    #         board[r][c]['fish'] -= 1
    #         board[fish.r][fish.c]['fish'] += 1
    # shark.move()
    #
    # print(fish)
    # print_board(board)