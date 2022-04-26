# 맞았습니다!!
import copy
N, M = map(int, input().split())

result = []
arr = []

def backtracking(length):
    if length == M:
        print(' '.join(map(str, arr)))
        return
    if arr:
        k = arr[-1]
    else:
        k = 1
    for i in range(k, N+1):
        arr.append(i)
        backtracking(length+1)
        arr.pop()


backtracking(0)