## 아이디어 수정
# 보 유효성 판단, 기둥 유효성 판단 함수를 만들고
# 삭제, 추가 시 일단 실행을 시켜보고 주위에 유효성 깨지는 요소들이 있나 확인

# 보가 유효한지 확인하는 함수
from this import d


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

def is_column(state, x, y):
    # 해당 좌표가 기둥의 아래좌표가 아니었던 경우
    if y + 1 >= len(state) : return True
    
    if y == 0 : return True 
    if state[x][y][0] >=2 or state[x][y][1] > 0 :
        return True
    return False

# 삭제 또는 추가가 가능한지 여부를 boolean으로 리턴
def do_job(job, state, answer):
    x, y, a, b = job[0], job[1], job[2], job[3]
    is_ok = None
    if a == 0:
        # 기둥 설치
        if b == 1:
            state[x][y][0] += 1
            state[x][y+1][0] += 1
            if not is_column(state, x, y):
                state[x][y][0] -= 1
                state[x][y+1][0] -= 1
            else:
                answer.append(job[0:3])
        # 기둥 삭제
        elif b == 0:
            state[x][y][0] -= 1
            state[x][y+1][0] -= 1
            is_done = True
            # 위에 기둥이 있었다면 is_column 실행
            if state[x][y+1][0] > 0 :
                is_done = is_done and is_column(state, x, y+1)
            if state[x][y+1][1] > 0 :
                is_done = is_done and is_beam(state, x, y+1)
                is_done = is_done and is_beam(state, x-1, y+1)
            if is_done:
                answer.remove(job[0:3])
            else:
                state[x][y][0] += 1
                state[x][y+1][0] += 1
    if a == 1:
        # 보 설치
        if b == 1:
            state[x][y][1] += 1
            state[x+1][y][1] += 1
            if not is_beam(state, x, y):
                state[x][y][1] -= 1
                state[x+1][y][1] -= 1
            else:
                answer.append(job[0:3])
        # 보 삭제
        elif b == 0:
            state[x][y][1] -= 1
            state[x+1][y][1] -= 1
            
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