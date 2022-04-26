# 맞았습니다!!
import copy
N, M = map(int, input().split())

result = []
visited = [False] * (N+1)
arr = []

def backtracking(length):
    if length == M:
        result.append(copy.deepcopy(arr))
        return
    for i in range(1, N+1):
        if not visited[i]:
            arr.append(i)
            #print(arr)
            visited[i] = True
            backtracking(length+1)
            arr.pop()
            visited[i] = False


backtracking(0)

for permu in result:
    for element in permu:
        print(element, end=' ')
    print()