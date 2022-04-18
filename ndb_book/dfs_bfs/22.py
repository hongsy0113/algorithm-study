from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 해당 좌표가 유효한지 확인
def is_valid(pos, grid):
    n = len(grid)
    if 0<=pos[0]<n and 0<=pos[1]<n and grid[pos[0]][pos[1]] == 0:
        return True
    else:
        return False

# 회전 함수
# 가능한 모든 조합의 회전 결과 좌표를 리스트로 반환
def rotate(pos1, pos2, grid):
    result = []
    # 로봇이 가로방향인지 세로방향인지 확인
    # 가로방향 일 때
    if pos1[0] == pos2[0]:
        if pos1[1] < pos2[1]:
            left = pos1
            right = pos2
        else:
            left = pos2
            right = pos1
        # 왼쪽 좌표를 축으로
        if is_valid((right[0]-1, right[1]), grid) and is_valid((right[0]-1, right[1]-1),grid):
            result.append((left, (right[0]-1, right[1]-1)))
        if is_valid((right[0]+1, right[1]), grid) and is_valid((right[0]+1, right[1]-1), grid):
            result.append((left, (right[0]+1, right[1]-1)))
        # 오른쪽 좌표를 축으로
        if is_valid((left[0]-1, left[1]), grid) and is_valid((left[0]-1, left[1]+1), grid):
            result.append((right, (left[0]-1, left[1]+1)))
        if is_valid((left[0]+1, left[1]), grid) and is_valid((left[0]+1, left[1]+1), grid):
            result.append((right, (left[0]+1, left[1]+1)))
    # 세로 방향일 때
    else:
        if pos1[0] < pos2[0]:
            top = pos1
            bottom = pos2
        else:
            top = pos2
            bottom = pos1
        # 위 좌표를 축으로 
        if is_valid((bottom[0], bottom[1]-1), grid) and is_valid((bottom[0]-1, bottom[1]-1), grid):
            result.append((top,(bottom[0]-1, bottom[1]-1)))
        if is_valid((bottom[0], bottom[1]+1), grid) and is_valid((bottom[0]-1, bottom[1]+1), grid):
            result.append((top, (bottom[0]-1, bottom[1]+1)))
        # 아래 좌표를 축으로
        if is_valid((top[0], top[1]-1), grid) and is_valid((top[0]+1, top[1]-1), grid):
            result.append((bottom, (top[0]+1, top[1]-1)))
        if is_valid((top[0], top[1]+1), grid) and is_valid((top[0]+1, top[1]+1),grid):
            result.append((bottom, (top[0]+1, top[1]+1)))

    return result

def bfs(pos1, pos2, grid):
    n = len(grid)
    # queue에 들어가는 값
    # 현재 좌표1, 좌표2, 이전 좌표1, 좌표2, 단계 수
    queue = deque([(pos1, pos2, (0,0),(0,1), 0)])
    visited = []
    visited.append({pos1, pos2})
    while queue:
        pos1, pos2, prev_pos1, prev_pos2, step = queue.popleft()

        if pos1 == (n-1, n-1) or pos2 == (n-1,n-1):
            return step
            
        # 평행이동 고려
        for i in range(4):
            n_pos1 = (pos1[0] + dx[i], pos1[1] + dy[i])
            n_pos2 = (pos2[0] + dx[i], pos2[1] + dy[i])
            # next 좌표가 이동 가능 가능한 좌표인지 확인
            # 벽은 아닌지, 왔던 길 되돌아 가는 것은 아닌

            if is_valid(n_pos1, grid) and is_valid(n_pos2, grid): 
                
                if {n_pos1, n_pos2} not in visited:
                    queue.append((n_pos1, n_pos2, pos1, pos2, step+1))
                    visited.append({n_pos1,n_pos2})
        # 회전 고려
        for v in rotate(pos1, pos2, grid):
            n_pos1, n_pos2 = v
            # 이전 회전 다시 반복하는 것인지 확인
            #if (n_pos1 != prev_pos1 and n_pos2 != prev_pos2) or (n_pos1 != prev_pos2 and n_pos2 != prev_pos1):
            if {n_pos1, n_pos2} not in visited:
                queue.append((n_pos1, n_pos2, pos1, pos2, step+1))
                visited.append({n_pos1,n_pos2})

    return -1


def solution(board):
    answer = 0
    answer = bfs((0,0), (0,1), board)
    return answer


board = [
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0]
    ]
board = [
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0]
    ]
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]


print(solution(board))
