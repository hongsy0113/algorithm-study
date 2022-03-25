# 네트워크

def dfs(computers, com, visited):
    visited[com] = True
    print(com)
    for i, c in enumerate(computers[com]):
        if i != com and visited[i] == False and c==1:
            dfs(computers, i, visited)



def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(computers, i, visited)
            answer += 1
    return answer

computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
print(solution(n, computers))