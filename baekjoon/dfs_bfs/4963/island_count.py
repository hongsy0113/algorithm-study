from ast import Pass
import sys
sys.setrecursionlimit(10**5)

dx = [-1, 0, 1,  0, -1, 1,  1, -1]
dy = [ 0, 1, 0, -1,  1, 1, -1, -1]

def dfs(graph, v):
    global dx, dy
    # visited 대신 graph을 0으로 해서 땅에서 제외
    graph[v[0]][v[1]] = 0

    for i in range(len(dx)):
        new_x = v[0] + dx[i]
        new_y = v[1] + dy[i]
        if new_x >= 0 and new_y >=0 and new_x < len(graph) and new_y < len(graph[0]):
            if graph[new_x][new_y] == 1:
                dfs(graph, (new_x, new_y))

def solve():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if (w,h) == (0, 0):
            break
        graph = []
        count = 0
        for _ in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    dfs(graph, (i, j))
                    count += 1
        print(count)

if __name__ == '__main__':
    solve()
    