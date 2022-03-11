import sys
from unittest import result
sys.setrecursionlimit(10 ** 7)


def dfs(choices, x, cycle, visited):
    global result
    visited[x] = True
    cycle.append(x)
    next_student = choices[x]

    if visited[next_student]:
        if next_student in cycle:
            result += cycle[cycle.index(next_student):]
        return
    else:
        dfs(choices, next_student, cycle, visited) 


    
T = int(sys.stdin.readline())

# 결과 저장할 리스트
#result = []

for _ in range(T):
    result = []
    # 입력 파트
    n = int(sys.stdin.readline())

    choices = [0] + list(map(int, sys.stdin.readline().split()))
    
    visited = [True] + [False] * (n)
    for v in range(1, n+1):
        if visited[v] == False:
            # 해당 노드에 대해 탐색 후 팀이 만들어졌다면 학생 번호 리스트, 그렇지 않다면 빈리스트 반환
            dfs(choices,v, [], visited)
    

    print(n - len(result))




### dict 로 하다가 포기