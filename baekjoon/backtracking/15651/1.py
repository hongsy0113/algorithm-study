# 맞았습니다!!
import copy
N, M = map(int, input().split())

result = []
arr = []

def backtracking(length):
    if length == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        arr.append(i)
        backtracking(length+1)
        arr.pop()


backtracking(0)

# for permu in result:
#     for element in permu:
#         print(element, end=' ')
#     print()