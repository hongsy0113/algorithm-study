from collections import deque
import sys
input = sys.stdin.readline

# 우 하 좌 상
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(graph, red_start, blue_start, visited, new_visited):
    n = len(graph)
    m = len(graph[0])
    queue_red = deque([(red_start, 0)])
    queue_blue = deque([(blue_start, 0)])
    visited[red_start[0]][red_start[1]] = True

    while queue_red and queue_blue:
        (red_x, red_y), cnt = queue_red.popleft()
        (blue_x, blue_y), cnt = queue_blue.popleft()
        if cnt > 10: return -1
        # 해당 위치에서 각 방향으로 기울여본다.
        for i in range(4):
            result = ''
            step = 1
            red_stop = False
            blue_stop = False
            while True:
                changed = False
                if not red_stop:
                    temp_x, temp_y = red_x + step * dx[i], red_y + step * dy[i]
                    # 더이상 이동 가능한지 확인
                    if 0<=temp_x<n and 0<=temp_y<m and graph[temp_x][temp_y] != '#' and not visited[temp_x][temp_y]:
                        n_red_x = temp_x
                        n_red_y = temp_y
                        changed = True
                    else:
                        n_red_x = red_x + (step-1) * dx[i]
                        n_red_y = red_y + (step-1) * dy[i]
                        red_stop = True
                    if visited[temp_x][temp_y]:
                        break

                if not blue_stop:
                    temp_x, temp_y = blue_x + step * dx[i], blue_y + step * dy[i]
                    # blue 더 이상 이동가능한지 확인
                    # red가 먼저 이동하기 때문에 이동하려는 위치에 red가 이미 있으면 못 움직임
                    if 0<=temp_x<n and 0<=temp_y<m and graph[temp_x][temp_y] != '#' and not (temp_x == n_red_x and temp_y == n_red_y):

                        n_blue_x = temp_x
                        n_blue_y = temp_y
                        changed = True
                    else:
                        n_blue_x = blue_x + (step-1) * dx[i]
                        n_blue_y = blue_y + (step-1) * dy[i]
                        blue_stop = True
                # red가 먼저 이동하기 때문에 red는 일단 다음위치에 blue 있든 말든 이동
                # 그렇기 때문에 혹시 blue로 인해서 이동 불가능했는지 확인
                if n_red_x == n_blue_x and n_red_y == n_blue_y:
                    n_red_x, n_red_y = red_x + (step-1) * dx[i], red_y + (step-1) * dy[i]
                    n_blue_x, n_blue_y = blue_x + (step-1) * dx[i], blue_y + (step-1) * dy[i]
                    changed = False

                ## 구멍에 들어갔는지 확인
                if graph[n_red_x][n_red_y] == 'O':
                    result = 'success'
                    red_stop = True
                    n_red_x = -1
                    n_red_y = -1
                if graph[n_blue_x][n_blue_y] == 'O':
                    result = 'fail'
                # 이동이 없었다면 종료
                if not changed or result == 'fail':
                    break
                visited[n_red_x][n_red_y] = True

                step += 1

            if result == '' and (n_red_x != red_x or n_red_y != red_y):

                queue_red.append(((n_red_x, n_red_y), cnt+1))
                queue_blue.append(((n_blue_x, n_blue_y), cnt+1))
            if result == 'success':
                return cnt + 1
    return -1
def solution(board, n, m, red_pos, blue_pos):
    visited = [[False] * m for _ in range(n)]
    new_visited = set([red_pos, blue_pos])
    answer = bfs(board, red_pos, blue_pos, visited, new_visited)
    print(answer)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(input().strip())
        for j in range(m):
            if board[i][j] == 'B':
                blue_pos = (i, j)
            if board[i][j] == 'R':
                red_pos = (i, j)
    solution(board, n, m, red_pos, blue_pos)

