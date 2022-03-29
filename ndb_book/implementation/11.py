from collections import deque
import sys
input = sys.stdin.readline

# game_map : 2차원 배열, 사과가 있으면 -1, 없으면 0, 뱀이 지나가면 1
# turn_dict : 방향 변환 정보를 담고 있는 딕셔너리. 키는 시간이고, 값은 C
# snake_pos : 뱀의 현재 좌표를 담고 있는 큐
# 입력된 데이터를 통해 게임을 시뮬레이션 하는 함수
def solution(game_map, snake_pos, turn_dict):
    N = len(game_map)-1
    
    time = 0
    # 우, 하, 좌, 상 이동에 대한 dx, dy 배열
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # turn_idx를 통해 dx, dy에 접근. 뱀 방향 바뀌면 이 변수를 수정하자
    turn_idx = 0
    # 게임이 종료될 때까지 실행
    while True:
        x, y = snake_pos[-1]
        nx = x + dx[turn_idx]
        ny = y + dy[turn_idx]

        # 게임 종료 조건
        if nx<1 or nx>N or ny<1 or ny>N or game_map[nx][ny] == 1 :
            time += 1
            break
        
        snake_pos.append((nx, ny))
        
        # 사과 없을 때
        if game_map[nx][ny] == 0:
            prev_x, prev_y = snake_pos.popleft()
            game_map[prev_x][prev_y] = 0
        game_map[nx][ny] = 1
        # 디버그 용 print
        for i in range(1, N):
            print(game_map[i])
        print()
        ### 다 이동하고 나면 1초가 증가하고 그때 고개를 돌림
        time += 1
        if time in turn_dict:
            if turn_dict[time] == 'L':
                turn_idx = (turn_idx - 1) % 4
            elif turn_dict[time] == 'D':
                turn_idx = (turn_idx + 1) % 4

    return time

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    game_map = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(K):
        apple_x, apple_y = map(int, input().split())
        game_map[apple_x][apple_y] = -1
    L = int(input())
    turn_dict = {}
    for _ in range(L):
        X, C = input().split()
        turn_dict[int(X)] = C
    
    snake_pos = deque([(1, 1)])

    answer = solution(game_map, snake_pos, turn_dict)

    print(answer)