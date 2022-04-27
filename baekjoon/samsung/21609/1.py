import sys
input = sys.stdin.readline
import copy
from collections import deque

# ## 디버깅용 출력함수
def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

## 보드 안에 있는 좌표인지 확인용
def in_board(r, c, N):
    if 0<=r<N and 0<=c<N:
        return True
    else:
        return False

### 반시계방향 90도 회전 함수
### 임시로 deepcopy를 해두고 원래 board객체에 회전이 적용되도록(리턴문 없이)
def rotate(board):
    n = len(board)
    temp_board = copy.deepcopy(board)
    # 새로운 행은 이전 배열의 열에 해당함
    for r in range(n):
        temp_col = []
        for i in range(n):
            temp_col.append(temp_board[i][n-1-r])
        board[r] = temp_col

### 중력작용하는 함수
## 사라진 칸은 -2로 나타냄
def gravity(board):
    '''

    맨 밑에서 두번째 행부터 위로 탐색
    (-1이 아니라면) 내려갈 수 있을 때 까지 이동 시킨다
    내려 가게 되면 기존 자리 -2로 해서 위에 값들이 내려올 수 있도록
    '''
    n = len(board)
    for r in range(n-2, -1, -1):
        for c in range(n):
            if board[r][c] == -1 or board[r][c] == -2:
                continue

            temp = board[r][c]
            nr, nc = r, c
            while True:
                # 기존 칸 사라지게 하자
                board[nr][nc] = -2
                nr += 1
                # 한 칸 내려와봤는데 벗어나거나 벽이면 직전 칸에 값 적는다
                if not in_board(nr, nc, N) or board[nr][nc] != -2:
                    board[nr-1][nc] = temp
                    break


### 블록 그룹 클래스
class BlockGroup:
    def __init__(self, members, value, count):
        self.members = members
        self.value = value
        self.count = count

        ## 대표 좌표 설정
        r, c = self.get_pos()
        self.r = r
        self.c = c

        ## 무지개 개수 저장
        self.rainbow_cnt = self.get_rainbow_count()

    # 대표 좌표 설정하는 함수
    def get_pos(self):
        # 먼저 블록의 종류로 정렬하고, 행 번호, 열번호로 정렬
        self.members.sort(key = lambda x: (
                        -board[x[0]][x[1]],
                        x[0],
                        x[1]
                        ))
        # 대표 블록 설정
        return self.members[0][0], self.members[0][1]

    # 무지개 개수 count 하는 함수
    # 정렬에 필요
    def get_rainbow_count(self):
        cnt = 0
        for member in self.members:
            r, c = member[0], member[1]
            if board[r][c] == 0:
                cnt += 1
        return cnt

    def __str__(self):
        return f'r,c = ({self.r}, {self.c})'

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
## bfs 함수
# 주의 무지개 색은 여러개 들어가도 된다
def bfs(r, c, board, visited, value):
    visited[r][c] = True
    # 블록 그룹의 개수를 세기 위한 변수
    cnt = 1
    # 블록 그룹의 멤버를 관리하기 위한 리스트
    members = [(r,c)]
    # 역방향으로 이동 안하기 위해 prev 방향 저장
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 우선 board를 벗어나는지 확인
            if in_board(nr, nc, N):
                # 검은색 블록일 경우 탐색 종료
                if board[nr][nc] == -1:
                    continue
                # 무재개 블록인 경우
                if not visited[nr][nc] and board[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    members.append((nr, nc))
                    cnt += 1
                # 색깔 블록의 경우
                if not visited[nr][nc] and board[nr][nc] == value :
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    members.append((nr, nc))
                    cnt += 1

    return cnt, members

# 블록 그룹 찾는 함수
def find_block_groups(N, M, board):
    '''

    각 블록에 대해서 dfs/bfs를 해본다
    cnt와 방문한 정보리스트를 append해서 유지
    visited를 통해 이미 방문했거나 이미 포함된 칸은 제외할 수 있도록록

   '''
    block_groups = []
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # todo 아직 방문하지 않은 색깔 있는 칸에대해서만 탐색
            if not visited[r][c] and board[r][c] > 0:
                ## TODO 탐색
                cnt, members = bfs(r, c, board, visited, board[r][c])

                # 결과로 cnt, members 리스트 구하고, 값도 받는다
                # 블록그룹 객체 만든다.
                if cnt >=2:
                    blockgroup = BlockGroup(members, board[r][c], cnt)
                    block_groups.append(blockgroup)
                ### 무지개 블록은 visited 초기화 해줘야 한다.
                for rainbow_block in rainbow_blocks:
                    visited[rainbow_block[0]][rainbow_block[1]] = False

    return block_groups

def solution(N, M, board):
    global rainbow_blocks
    score = 0
    ## 더 이상 블록 그룹이 없을 떄까지 반복
    while True:

        #### 블록 그룹을 찾아서 리스트로 반환
        block_groups = find_block_groups(N, M, board)
        ## 블록 그룹이 더이상 없다면 종료
        if len(block_groups) == 0:
            return score

        #### lambda함수로 정렬해서 가장 큰 블록 그룹 찾는다.
        block_groups.sort(key = lambda x: (
            x.count,
            x.rainbow_cnt,
            x.r,
            x.c
        ))
        ## 정렬을 역순으로 했으므로 pop을 하면 가장 우선순위의 객체가 나온다
        biggest_group = block_groups.pop()

        #### 해당 블록 그룹 제거
        for block in biggest_group.members:
            board[block[0]][block[1]] = -2

        #### 점수 증가
        score += biggest_group.count ** 2
        #### 3. 중력 작용
        gravity(board)
        #### 4. 90도 회전
        rotate(board)

        #### 5. 중력 작용
        gravity(board)
        print_board(board)

        ## rainbow blocks 갱신
        rainbow_blocks = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    rainbow_blocks.append((r, c))


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    rainbow_blocks = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(N):
            ## 무지개 칸은 따로 관리
            if board[i][j] == 0:
                rainbow_blocks.append((i, j))

    ## solution 함수
    score = solution(N, M, board)
    print(score)