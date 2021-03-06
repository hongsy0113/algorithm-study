# 맞았습니다!!

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

result = set([])
arr = []
visited = [False] * N

def backtracking(length):
    if length == M:
        if not tuple(arr) in result:
            print(' '.join(map(str, arr)))
            result.add(tuple(arr))
        return

    for i in range(0, N):
        if not visited[i]:

            arr.append(num_list[i])
            visited[i] = True
            backtracking(length + 1)
            arr.pop()
            visited[i] = False



backtracking(0)