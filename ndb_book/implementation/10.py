def list_shift (lst, y):
    if y>0:
        left = [0] * y
        right = lst[:len(lst)-y]
        return left+lst
    elif y<0:
        for i in range(-y):
            del lst[0]
            lst.append(0)
        return lst
    else: return lst

## TODO 이동 함수 먼저 구현
def move_key(key, x, y):
    # TODO : x 방향 이동 
    if x<0:
        for i in range(-x): 
            del key[0]
            key.append([0]*len(key[0]))
    elif x>0:
        up = [[0]*len(key) for _ in range(x)]
        #down = key[:len(key)-x]
        key = up + key
    # TODO : y 방향 이동
    for i in range(len(key)):
        key[i] = list_shift(key[i], y)

    return key

def rotate_90(key):
    N = len(key)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = key[r][c]
    return ret

## 기준이 될 홈 좌표 구하는 함수
def get_holl (lock, n):
    flag= False
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                flag = True
                return i, j
    # 수정한 부분
    if flag == False: return -1, -1
# 실제 move, rotation 할 때는 key를 copy해두자
def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    # TODO lock의 첫번째 홈에다가 key의 모든 돌기들을 넣어본다...
    # 먼저 기준이 될 홈 정한다
    lock_x, lock_y = get_holl(lock, n)
    ## 수정
    if lock_x == -1: return False
    ## TODO : key 를 탐색하면서 돌기가 있을 경우 이동해서 lock_x, lock_y에 맞춰 본다
    for _ in range(4):
        key = rotate_90(key)
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    temp_key = key.copy()
                    x, y = (lock_x - i, lock_y - j)
                    print('x, y', x, y)
                    temp_key = move_key(temp_key, x, y)
                    print(temp_key)
                    # TODO: lock의 모든 격자에 대해서 맞는지 확인
                    flag = 0
                    for lx in range(n):
                        for ly in range(n):
                            try:
                                if lock[lx][ly] + temp_key[lx][ly] != 1:
                                    flag = 1
                                    break
                            except IndexError:
                                flag = 1
                                break
                        if flag == 1: break
                    if flag == 0: 
                        print('real true')
                        return True
    return answer



key =[
    [0, 0, 0], 
    [1, 0, 0], 
    [0, 1, 1]
]
# key = [
#     [0, 1, 0], 
#     [1, 0, 0], 
#     [1, 0, 0]
# ]
lock = [
    [1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 1]
]
lock = [[1]]
# print(rotate_90(key))

print(solution(key, lock))

# test_key = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 1]
# ]
# print(move_key(test_key, 3, 3))
