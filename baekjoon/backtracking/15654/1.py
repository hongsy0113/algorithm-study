# 맞았습니다!!

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

result = []
arr = []
visited = [False] * N

def backtracking(length):
    if length == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if not visited[i]:
            arr.append(num_list[i])
            visited[i] = True
            backtracking(length+1)
            arr.pop()
            visited[i] = False



backtracking(0)