import sys
input = sys.stdin.readline

# 가로선 놓을 수 있는지 없는지 판단하는 함수
def line_valid (line, vertical_lines):
    if line in vertical_lines:
        return False
    a, b = line[0], line[1]
    if (a, b - 1) in vertical_lines or (a, b + 1) in vertical_lines:
        return False
    return True

## 사다리탄 결과가 i가 i로 잘 가는지 확인하는 함수
def play_game(N, H, vertical_lines):
    for i in range(1, N+1):
        # depth 는 현재 진행의 깊이를 나타내고, n 은 가로선 위치를 나타냄
        depth = 1
        n = i
        while depth <= H:
            temp = n
            if (depth, n) in vertical_lines:
                temp = n + 1
            elif (depth, n-1) in vertical_lines:
                temp = n - 1
            n = temp
            depth += 1
        if n != i:
            return False
    return True

# 조합 만드는 함수
def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        first = arr[i]
        rest_arr = arr[i+1:]
        for C in combinations(rest_arr, n-1):
            result.append([first] + C)

    return result

# 조합 만드는 함수
def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        first = arr[i]
        rest_arr = arr[i+1:]
        for C in combinations(rest_arr, n-1):
            result.append([first] + C)

    return result

def solution(N, M, H, vertical_lines):

    # TODO 0: 하나도 안 놓고 먼저 실행
    if play_game(N, H, vertical_lines):
        return 0
    # TODO 1: 한개 놓는 거 먼저 진행
    for a in range(1, H+1):
        for b in range(1, N):
            # # 이미 설치된 가로선이라면 skip
            # if (a,b) in vertical_lines:
            #     continue
            # # 좌우 연속되어 있는지 확인
            # if (a, b-1) in vertical_lines or (a, b+1) in vertical_lines:
            #     continue
            if not line_valid((a,b), vertical_lines):
                continue
            # 가로선을 추가해본다
            vertical_lines.add((a,b))
            # 사다리 게임을 실행시켜보고 성공한다면 바로 1 리턴
            if play_game(N, H, vertical_lines):
                return 1
            # 실패한다면 추가한 가로선 삭제하고 다시 다음 case 진행
            else:
                vertical_lines.remove((a,b))

    possible_lines = []
    # 모든 가능한 lines 구해보자
    for a in range(1, H + 1):
        for b in range(1, N):
            if not (a, b) in vertical_lines:
                possible_lines.append((a, b))
    possible_lines = set(possible_lines)

    # TODO 2: 두개 놓는 거 진행
    for case in combinations(list(possible_lines), 2):
        # line 유효한지 확인
        is_valid = True
        for line in case:
            if not line_valid(line, vertical_lines):
                is_valid = False
                break
        # line 유효하지 않다면 다음 케이스 실행
        if not is_valid:
            continue
        # 가로선 두개 추가해본다
        for line in case:
            vertical_lines.add(line)
        # 사다리 게임을 실행시켜보고 성공한다면 바로 1 리턴
        if play_game(N, H, vertical_lines):
            return 2
        # 실패한다면 추가한 가로선 삭제하고 다시 다음 case 진행
        else:
            for line in case:
                vertical_lines.remove(line)
    # TODO 3 : 세 개 놓기
    for case in combinations(list(possible_lines), 3):
        # line 유효한지 확인
        is_valid = True
        for line in case:
            if not line_valid(line, vertical_lines):
                is_valid = False
                break
        # line 유효하지 않다면 다음 케이스 실행
        if not is_valid:
            continue
        # 가로선 두개 추가해본다
        for line in case:
            vertical_lines.add(line)
        # 사다리 게임을 실행시켜보고 성공한다면 바로 1 리턴
        if play_game(N, H, vertical_lines):
            return 3
        # 실패한다면 추가한 가로선 삭제하고 다시 다음 case 진행
        else:
            for line in case:
                vertical_lines.remove(line)

    return -1


def dfs(cnt, a, b, N, M, vertical_lines):
    global answer
    if play_game(N, H, vertical_lines):
        answer = min(answer, cnt)
        return
    elif cnt >= 3 or answer <= cnt:
        return

    for i in range(a, H+1):
        k = b if i == a else 0
        for j in range(k, N):
            if line_valid((i,j), vertical_lines):
                vertical_lines.add((i,j))
                dfs(cnt+1, i, j, N, M, vertical_lines)
                vertical_lines.remove((i,j))



if __name__ == '__main__':
    N, M, H = map(int, input().split())
    vertical_lines = []
    for _ in range(M):
        a, b = map(int, input().split())
        vertical_lines.append((a,b))
    answer = 4
    #print(solution(N, M, H, set(vertical_lines)))
    dfs(0, 1, 1, N, M, set(vertical_lines))
    print(answer if answer < 4 else -1)