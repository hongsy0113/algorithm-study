# 맞았습니다!!

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

result = []
arr = []
checked = [False] * N


def backtracking(length):
    if length == M:
        print(' '.join(map(str, arr)))
        return
    overlap = 0

    for i in range(N):

        # 전에 있는 수보다 클 경우에만 탐색
        if overlap != num_list[i] :
            arr.append(num_list[i])
            checked[i] = True
            overlap = num_list[i]
            backtracking(length+1)
            checked[i] = False
            arr.pop()



backtracking(0)