from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(place, x, y, visited):
    result = 1
    visited[x][y] =  True

    # 깊이 정보도 같이 담는다
    queue = deque([[(x,  y), 0]])
    while queue:
        v, depth = queue.popleft()
        depth += 1
        if depth > 2: break
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0<=nx<len(place) and 0<=ny<len(place):
                if visited[nx][ny] == False and place[nx][ny] == 'P':
                    return 0
                if visited[nx][ny] == False and place[nx][ny] != 'X':
                    queue.append([(nx,ny),depth])

                    visited[nx][ny] = True

    return result

def solution_per_place(place):
    for i in range(5):
            for j in range(5):
                visited = [[False] * 5 for _ in range(5)]
                if place[i][j] == 'P':
                    result = bfs(place, i, j, visited)
                    if result == 0: return 0
    return 1

def solution(places):
    answer = []
    for k in range(5):
        answer.append(solution_per_place(places[k]))
    return answer


places = [
    [
        "POOOP", 
        "OXXOX", 
        "OPXPX", 
        "OOXOX", 
        "POXXP"
    ], 
    [
        "POOPX", 
        "OXPXP", 
        "PXXXO", 
        "OXXXO", 
        "OOOPP"
    ], 
    [
        "PXOPX", 
        "OXOXP", 
        "OXPOX", 
        "OXXOP", 
        "PXPOX"
    ], 
    [
        "OOOXX", 
        "XOOOX", 
        "OOOXX", 
        "OXOOX", 
        "OOOOO"
    ], 
    [
        "PXPXP", 
        "XPXPX", 
        "PXPXP", 
        "XPXPX", 
        "PXPXP"
    ]
]
print(solution(places))