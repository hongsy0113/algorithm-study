## 아이디어 수정
# 보 유효성 판단, 기둥 유효성 판단 함수를 만들고
# 삭제, 추가 시 일단 실행을 시켜보고 주위에 유효성 깨지는 요소들이 있나 확인

# 아이디어 추가 : state 에 기둥, 보 마다 하나 좌표만 표시하자. 좌우. 상하 통일
# 보가 유효한지 확인하는 함수

def is_beam (state, x, y):
    # 한쪽 끝 기둥이어야 함. 기둥 + 보 인 경우 고려해서 % 연산
    if state[x][y-1]%2 == 1 or state[x+1][y-1]%2 == 1:
        return True
    elif state[x-1][y] >= 2 and state[x+1][y] >= 2:
        return True
    else: 
        return False

def is_column(state, x, y):
    if y == 0 : return True 
    # 아래가 기둥인 경우
    if state[x][y-1] % 2 == 1:
        return True
    if state[x][y] >= 2:
        return True
    if x-1 >= 0 and state[x-1][y] >= 2:
        return True
    return False

# 삭제 또는 추가가 가능한지 여부를 boolean으로 리턴
def do_job(job, state, answer):
    x, y, a, b = job[0], job[1], job[2], job[3]
    is_ok = None
    if a == 0:
        # 기둥 설치
        if b == 1:
            state[x][y] += 1
            if not is_column(state, x, y):
                state[x][y] -= 1
            else:
                answer.append(job[0:3])
        # 기둥 삭제
        elif b == 0:
            state[x][y] -= 1 
            is_done = True
            # 위에 기둥이 있었다면 is_column 실행
            if state[x][y+1] % 2 == 1:
                is_done = is_done and is_column(state, x, y+1)
            # 보가 있다면 is_beam 실행
            if state[x][y+1] >= 2:
                is_done = is_done and is_beam(state, x, y+1)
            if x-1>=0 and state[x-1][y+1] >=2 :
                is_done = is_done and is_beam(state, x-1, y+1)

            if is_done:
                answer.remove(job[0:3])
            else:
                state[x][y] += 1
    if a == 1:
        # 보 설치
        if b == 1:
            state[x][y] += 2
            if not is_beam(state, x, y):
                state[x][y] -= 2
            else:
                answer.append(job[0:3])
        # 보 삭제
        elif b == 0:
            state[x][y] -= 2
            is_done = True
            # 보위에 기둥 있으면 확인
            if state[x][y] % 2 == 1:
                is_done = is_done and is_column(state,x,y)
            if state[x+1][y] % 2 == 1:
                is_done = is_done and is_column(state,x+1,y)
            # 양옆 보 확인
            if x-1>=0 and state[x-1][y] >=2:
                is_done= is_done and is_beam(state, x-1, y)
            if x+1 <= len(state) and state[x+1][y]>=2:
                is_done= is_done and is_beam(state, x+1, y)
            
            if is_done:
                answer.remove(job[0:3])
            else:
                state[x][y] += 2
    return answer

def solution(n, build_frame):
    answer = []
    # 2차원 리스트로 구조물 상태 표현
    # 0: noting, 1은 기둥, 2는 보, 3:기둥+보 
    state = [[0] * (n+1) for _ in range(n+1)]


    for job in build_frame:
        do_job(job, state, answer)
        print(answer)
    
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    print(answer)
    return answer


build_frame  =[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5

solution(n, build_frame)
