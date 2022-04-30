import sys
input = sys.stdin.readline

# →, ↑, ↓, ←,
dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]

# board를 정해진 순서대로 순회하는 함수
# 1차원 리스트 marbels에 구슬 번호를 순차적으로 저장
def traversal (board, N):
    marbles = [0] * (N**2)

    # marbels에 저장한 idx를 idx 변수로 관리
    center_r, center_c = (N+1) // 2, (N+1) // 2
    marbles[1] = board[center_r][center_c - 1]
    marbles[2] = board[center_r + 1][center_c - 1]
    # 최대 몇 칸 까지 길이가 가는지
    # →, ↑, ←, ↓
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    idx = 3
    d = 0
    r, c = center_r + 1, center_c - 1
    for k in range(2, N):
        # k칸 만큼 두 번 이동 한다
        for _ in range(2):
            for _ in range(k):
                nr = r + dx[d]
                nc = c + dy[d]
                marbles[idx] = board[nr][nc]
                idx += 1
                r, c = nr, nc
            d = (d+1) % 4
    ## 마지막에 제일 첫번째 행도 탐색해준다
    d = 2
    for _ in range(N-1):
        nr = r + dx[d]
        nc = c + dy[d]
        marbles[idx] = board[nr][nc]
        idx += 1
        r, c = nr, nc

    return marbles

# 마법 시전하는 함수
# 마법의 시전되는 위치가 몇번인지, 즉 1차원 리스트 상에서 몇번째인지 찾는다
def blizzard(board, marbles ,command):
    d, s = command[0], command[1]
    if d == 4:
        k = 5
    elif d == 1:
        k = 7
    elif d == 2:
        k = 3
    elif d == 3:
        k = 1

    remove_dict = {}
    marble_num = 0
    # 한칸씩 멀리갈때마다 규칙있다
    # 칸수를 s 라고 했을 때, 8 * (s-1) + k 만큼 더해주는 수열
    for i in range(1, s+1):
        marble_num += 8 * (i-1) + k
        marbles[marble_num] = -1
        # pos_set.add(marble_num)


## 시간초과 막기위해서 del 과정을 최적화해보자
# 차라리 새롭게 리스트 만드는게 나을 수도 o(n)
# remove_list set으로 가정
def remove_and_create(remove_dict, marbles):
    new_marbles = [0]
    for i in range(1, len(marbles)):
        if not i in remove_dict:
            new_marbles.append(marbles[i])

    for _ in range(N ** 2 - len(new_marbles)):
        new_marbles.append(0)

    return new_marbles

def arrange(marbles):
    del_cnt = marbles.count(-1)
    marbles = [marble for marble in marbles if marble != -1]
    marbles.extend([0]*del_cnt)
    return marbles

def solution(board, N, commands):
    ### board를 순회해서 구슬 번호 리스트를 1차원 리스트로 만든다
    marbles = traversal(board, N)
    bomb_cnt = {1: 0, 2: 0, 3: 0}
    ## commands의 command에 대해서 반복을 돌린다
    for command in commands:
        ## d, s 에 대해서 마법을 시전한다.
        blizzard(board, marbles, command)
        marbles = arrange(marbles)
        ### marbels 상에서의 idx 구하고 삭제한다
        #marbles = remove_and_create(to_remove_dict, marbles)

        ## 구슬이 폭발한다
        # 더이상 폭발 안 할 떄까지 반복

        while True:
            is_bombed = False
            cnt = 1
            num = marbles[1]
            # 터져야하는 구슬의 idx가 들어간다
            # bomb_set = set([])
            # temp_bomb_set = set([1])
            bomb_set = {}
            temp_bomb_set = set([1])
            for i in range(2, len(marbles)):
                if marbles[i] == 0:
                    break
                if marbles[i] == num:
                    cnt += 1
                    temp_bomb_set.add(i)
                else:
                    ## cnt가 네개 이상이었다면
                    if cnt >= 4:
                        for idx in temp_bomb_set:
                            marbles[idx] = -1
                        is_bombed = True
                        temp_bomb_set = set([i])
                        # cnt 누적
                        bomb_cnt[num] += cnt
                        cnt = 1
                    else:
                        # temp list 초기화
                        temp_bomb_set = set([i])
                        cnt = 1
                        num = marbles[i]

            if not is_bombed:
                break

            # 지워진 곳을 -1로 하고 한번에 정리하는 함수 사용
            marbles = arrange(marbles)

            #marbles = remove_and_create(bomb_set, marbles)
            # ### remove_crate 함수 사용
            # marbles = remove_and_create(bomb_set, marbles)

        # marbels 사용
        # 폭발한 구슬 수 count 해야 함

        # 구슬 변화 단계
        # 새롭게 구슬 리스트를 만드는게 시간복잡도 더 적을 듯
        new_marbles = [0]
        # 먼저 그룹을 만들고
        num = marbles[1]
        cnt = 1
        for i in range(2, len(marbles)):
            if marbles[i] == 0:
                break
            if marbles[i] == num:
                cnt += 1
            else:
                # 기존 그룹을 groups에 append
                A = cnt
                B = num
                new_marbles.append(A)
                new_marbles.append(B)
                cnt = 1
                num = marbles[i]
        # 그 그룹을 순회하면서 new_marbles를 만들자
        for _ in range(N**2 - len(new_marbles)):
            new_marbles.append(0)
        marbles = new_marbles
    score = 0
    for key, value in bomb_cnt.items():
        score += key * value

    return score


if __name__ == '__main__':
    ## 입력 받는 단계
    N, M = map(int, input().split())
    board = [[0] * (N+1)]
    for _ in range(N):
        board.append([0] + list(map(int, input().split())))
    commands = []
    for _ in range(M):
        commands.append(tuple(map(int, input().split())))

    print(solution(board, N, commands))
