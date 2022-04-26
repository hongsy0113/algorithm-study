## 맞았습니다!!
import copy
N, M = map(int, input().split())

result = []
visited = [False] * (N+1)
arr = []

def backtracking(length):
    if length == M:
        result.append(copy.deepcopy(arr))
        return
    # 수열이 오름차순으로 되어야 하므로
    # 탐색을 이전 수보다 큰 범위만 진행
    if arr:
        k = arr[-1]
    else:
        k = 1
    for i in range(k, N+1):
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