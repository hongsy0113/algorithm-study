# 맞았습니다!!

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

result = []
arr = []

def backtracking(length):
    if length == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        prev = arr[-1] if arr else num_list[0]
        # 전에 있는 수보다 클 경우에만 탐색
        if num_list[i] >= prev:
            arr.append(num_list[i])
            backtracking(length+1)
            arr.pop()



backtracking(0)