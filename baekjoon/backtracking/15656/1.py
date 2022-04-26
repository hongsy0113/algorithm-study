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

        arr.append(num_list[i])
        backtracking(length+1)
        arr.pop()



backtracking(0)