import sys
sys.setrecursionlimit(10**5)

# 더 먼 곳 먼저
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(graph, v, dp):
    if v[0] == len(graph)-1 and v[1] == len(graph[0])-1:
        return 1
    if dp[v[0]][v[1]] != -1:
        return dp[v[0]][v[1]]
    dp[v[0]][v[1]] = 0
    
    for i in range(4):
        new_pos = (v[0]+dx[i], v[1]+dy[i])
        if 0<=new_pos[0]< len(graph) and 0<=new_pos[1]<len(graph[0]):
            # 오르막길 인 경우에만 탐색 가능
            if graph[new_pos[0]][new_pos[1]] < graph[v[0]][v[1]]:
                # 이미 방문한 노드의 경우에는 추가 탐색이 필요 없으므로 dp 값만 증가
                dp[v[0]][v[1]] += dfs(graph, new_pos, dp)
    return dp[v[0]][v[1]] 

def solve():
    m, n = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [[-1] * n for _ in range(m)]
    print(dfs(graph, (0,0), dp))
    

if __name__ == '__main__':
    solve()