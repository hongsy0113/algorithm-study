import sys
input = sys.stdin.readline

## 디버깅용 출력함수
def print_room(room):
    n = len(room)
    for i in range(1, n):
        print(room[i][1:])
    print()

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 입력 좌표가 교실을 벗어났는지 확인하는 함수
def in_room(r,c):
    if 1<=r<=N and 1<=c<=N:
        return True
    else:
        return False

'''
정렬 기준 lambda 함수에 쓰일 함수들을 정의하자
각각은 문제 설명의 1,2,3,4번에 해당한다
입력은 (r,c) 좌표이고 출력은 어떠한 우선순위 정수값이다. 
'''

### 1. 좋아하는 학생이 얼마나 인접해 있는지
# 현재 몇번을 배치시킬 차례인지는 student 인자 사용
# 실제 람다함수를 사용할 때는 인자에 값을 넣어서
def preference_adj_cnt(r, c, student):
    cnt = 0
    # 상하좌우를 확인하며 인접한 좋아하는 사람 수 count
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_room(nr, nc):
            if room[nr][nc] in preference_dict[student]:
                cnt += 1

    return cnt

### 2. 인접한 칸 중에서 빈칸이 얼마나 있는지
def empty_adj_cnt(r, c, student):
    cnt = 0
    # 상하좌우를 확인하며 인접한 빈 칸 수 count
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_room(nr, nc):
            if room[nr][nc] == 0:
                cnt += 1

    return cnt

### 만족도 총합 구하는 함수
def get_total_pref(N,room, preference_dict):
    total_score = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            cnt = 0
            student = room[r][c]
            # 각 student가 몇명의 좋아하는 사람과 인접해있는지 count
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if in_room(nr, nc) and room[nr][nc] in preference_dict[student]:
                    cnt += 1
            if cnt > 0:
                total_score += 10 ** (cnt-1)

    return total_score

def solution(N, student_order, preference_dict):

    ### 빈 공간의 좌표들 저장
    empty_seat = []
    for r in range(1, N+1):
        for c in range(1, N+1):
            empty_seat.append((r,c))

    ###########
    ### student_list의 각 학생에 대해서 자리 배정
    for student in student_order:
        ### lambda 함수로 빈 좌석을 정렬 한 후, 가장 우선 순위 좌석 선정
        ## pop 연산을 활용하기 위해서 거꾸로 정렬
        empty_seat.sort(key= lambda x:
                        (
                            preference_adj_cnt(x[0], x[1], student),
                            empty_adj_cnt(x[0], x[1], student),
                            -x[0],
                            -x[1]
                         ))

        to_seat = empty_seat.pop()
        ## 해당 좌석 좌표의 room 에 stuent 번호 대입
        room[to_seat[0]][to_seat[1]] = student
        ## empty_set 리스트에서 해당 좌석 좌표 remove(pop을 통해 이미 처리됨)

    ### 마지막에 점수를 매긴다
    return get_total_pref(N, room, preference_dict)

if __name__ == '__main__':
    N = int(input())
    ## 딕셔너리에 어떤 학생이 누구 좋아하는지 저장
    preference_dict = {}
    ## 리스트에 자리 배치하는 학생 순서대로 저장
    student_order = []
    for _ in range(N**2):
        student, pref1, pref2, pref3, pref4 = map(int, input().split())
        student_order.append(student)
        preference_dict[student] = [pref1, pref2, pref3, pref4]
    ### 교실 정보 저장위한 2차원 리스트
    room = [[0] * (N + 1) for _ in range(N + 1)]

    print(solution(N, student_order, preference_dict))