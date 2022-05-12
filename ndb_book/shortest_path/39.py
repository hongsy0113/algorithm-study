def print_board(board):
    n = len(board)
    for i in range(n):
        print(board[i])
    print()

import heapq
INF = int(1e9)

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(graph, n, distance):
    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))
    distance[0][0] = graph[0][0]

    while q :
        dist, (r, c) = heapq.heappop(q)
        if distance[r][c] < dist:
            continue

        ## 인접 노드들 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            ## board 벗어나는지 확인
            if not (0<=nr<n and 0<=nc<n):
                continue

            cost = dist + graph[nr][nc]
            if cost < distance[nr][nc]:
                distance[nr][nc] = cost
                heapq.heappush(q, (cost, (nr, nc)))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        board = []
        for _ in range(N):
            board.append(list(map(int, input().split())))
        distance = [[INF] * N for _ in range(N)]
        dijkstra(graph=board, n=N, distance=distance)

        print(distance[N-1][N-1])