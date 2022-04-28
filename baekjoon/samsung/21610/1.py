import sys
input = sys.stdin.readline

# 디버깅용 출력함수
def print_board(board):
    for i in range(1, N+1):
        print(board[i][1:])
    print()

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 0부터 순서대로 ↙, ←, ↖, ↑, ↗, →, ↘, ↓,
dr = [1, 0, -1, -1, -1, 0, 1, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0]

class Cloud:
    # 구름의 좌표들이 담긴 list를 파라미터로 받는다
    def __init__(self, members):
        self.members = members
        self.size = len(members)

    ### 1에서 구름 이동시키는 함수
    ## 인자로 d, s를 받는다
    def move(self, d, s):
        for member in self.members:
            nr, nc = self._move(member[0], member[1], d, s)
            member[0], member[1] = nr, nc

    ## 구름 한개를 이동시키는 함수,
    # move 함수의 내장함수로 쓰인다
    # 구름의 좌표를 받고 새롭게 이동한 좌표를 반환
    def _move(self, r, c, d, s):
        if d == 8: d = 0
        nr = r + s * dr[d]
        nc = c + s * dc[d]

        # 칸을 벗어나는 경우에는 나머지 연산자로 계산 가능
        nr = nr % N if nr % N != 0 else N
        nc = nc % N if nc % N != 0 else N

        return nr, nc

    # 2에서 구름 비내리는 함수
    def rain(self):
        for member in self.members:
            board[member[0]][member[1]] += 1

        # 5에서 구름이 사라진 칸인지 아닌지 확인하기 위해서 리턴 일단
        return self.members

    # 3에서 구름 사라지게 하는 함수
    # 현재로서는 딱히 필요 없을 듯

    # 디버기용
    # 구름의 좌표들을 출력하도록
    # def __str__(self):
    #     string = ''
    #     for member in self.members
    #     return self.members

## 최종 물의 양 합 구하는 함수
def get_total_water(baord):
    total_water = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            total_water += board[r][c]
    return total_water

# 구름 좌표들은 리스트의 리스트로 관리하고 이름은 members로 통일
## main solution 함수
def solution(N, M, board, commands):
    ## TODO 0. 초기 구름을 생성한다
    members = [[N, 1], [N, 2], [N-1, 1], [N-1, 2]]
    cloud = Cloud(members)
    ## commands의 각 명령을 실행한다
    for m in range(M):
        print(f'{m+1} 번쨰 ----------------- ')
        ## todo 1. 모든 구름을 이동시킨다
        d, s = commands[m][0], commands[m][1]
        cloud.move(d, s)
        print("1. 구름 이동 후 ")
        print(cloud.members)
        ## todo 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        # 4를 위해서 물이 증가한 칸들을 저장
        prev_members = cloud.members
        cloud.rain()

        print('비 내린 후')
        print_board(board)
        ## todo 3. 구름이 모두 사라진다.

        ## todo 4. 물복사 마법을 시전한다
        # 물이 증가한 각 칸에 대해서 반복문 실행
        for member in prev_members:
            cnt = 0
            r, c = member[0], member[1]
            # 해당 칸의 대각산 방향 좌표들 중 물있는 개수 구한다
            for i in range(0, 8, 2):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<nr<=N and 0<nc<=N and board[nr][nc] > 0:
                    cnt += 1
            # 그 개수 만큼 해당 칸의 물의 양 증가
            board[r][c] += cnt
        print('물 복사 후')
        print_board(board)
        # todo 5
        new_members = []
        # 바구니의 저장된 물이 2 이상인 곳들을 찾으면서 2를 감소시키고 새 구름 좌표 set에 add
        # 3에서 구름 사라진 칸이었었는지도 확인
        for r in range(1, N+1):
            for c in range(1, N+1):
                if board[r][c] >= 2 and not [r, c] in prev_members:
                    board[r][c] -= 2
                    new_members.append([r, c])
        # 구름 객체를 새롭게 생성
        cloud = Cloud(new_members)
        print('최종 상태')
        print_board(board)
        print(new_members)

    return get_total_water(board)

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [[0] * (N+1)]
    commands = []
    for _ in range(N):
        board.append([0] + list(map(int, input().split())))

    for _ in range(M):
        commands.append(tuple(map(int, input().split())))

    answer = solution(N, M, board, commands)
    print(answer)