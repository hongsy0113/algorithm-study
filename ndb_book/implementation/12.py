# 보가 유효한지 확인하는 함수
def is_beam (state, x, y):
    # 좌표가 범위를 벗어난 경우
    if x<0 or y<0 or (x+1)>= len(state) or (y+1)>= len(state): return True
    # 보가 아니다. 해당 좌표가 보의 왼쪽이 아니라는 뜻. 즉, 보가 없어서 괜찮다
    if not (state[x][y][1] > 0 and state[x+1][y][1]>0): return True 
    if state[x][y][0] > 0 or state[x+1][y][0] >0:
        return True
    elif state[x][y][1] >= 2 and state[x][y][1] >= 2:
        return True
    else: return False

# 삭제 또는 추가가 가능한지 여부를 boolean으로 리턴
def is_available(job, state):
    x, y, a, b = job[0], job[1], job[2], job[3]
    is_ok = None
    if a == 0:
        # 기둥 설치
        if b == 1:
            # 바닥위에 있거나 보의 한쪽 끝 부분 위에 있거나 다른 기둥 위에 있거나
            if y == 0 or state[x][y][0] != 0 or state[x][y][1] != 0:
                is_ok = True
            else:
                is_ok = False
        # 기둥 삭제
        elif b == 0:
            # 기둥 위에 뭐가 있는 지 확인해야 한다
            # 위에 기둥이 있다면 false
            if state[x][y+1][0] > 0:
                is_ok = False
            # 기둥 위에 보가 있으면 고려해야 할 경우가 많아서 따로 함수로 뺌
            # 기둥을 임시로 삭제해 보고 그 위에 있는 보들이 유효하다면 기둥 삭제 가능
            elif state[x][y+1][1] >= 1:
                state[x][y+1][0] -= 1
                if is_beam(state, x,y+1) and is_beam(state, x-1, y+1):
                    is_ok = True
                else:
                    is_ok = False
                state[x][y+1][0] += 1
    if a == 1:
        # 보 설치
        if b == 1:
            # 한쪽 끝 부분이 기둥 위에 있거나, 
            # 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야
            if state[x][y][0] > 0:
                is_ok = True
            elif state[x][y][1] > 0 and state[x+1][y][1] > 0:
                is_ok = True
            else:
                is_ok = False
        # 보 삭제
        elif b == 0:
            
            pass
    return is_ok
def solution(n, build_frame):
    answer = [[]]
    # 3차원 리스트로 구조물 상태 표현
    # 각 좌표마다 길이 2의 리스트를 가지도록
    # 길이 2 리스트는 기둥과 보의 개수를 나타낸다.
    state = [[[0,0]] * (n+1) for _ in range(n+1)]


    for job in build_frame:
        # TODO : 기둥 관련인지 보 관련인지 확인

        # TODO: 기둥이면 기둥, 보면 보 관련 유효여부 체크 함수 실행

        # TODO : 유효하다면 삭제, 추가에 맞게 answer 에 반영
        pass

    return answer

t = {'기둥':2, '보':3}
n= 5
test =  [[[0,0]] * (n+1) for _ in range(n+1)]
t['기둥'] = 4
print(test)