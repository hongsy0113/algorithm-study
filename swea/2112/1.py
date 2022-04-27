# 보호필름
import sys
sys.stdin = open("sample_input.txt", "r")

## 디버깅용 출력 함수
def print_films(films):
    D = len(films)
    for i in range(D):
        print(films[i])
    print()

## 하나의 약품에 대해서 막을 변경하는 함수 필요
# 입력: films, D, W, K, r, type
# r은 막의 위치, type은 0 또는 1로 a인지 b인지
def change_film(films, r, type, W):
    for c in range(W):
        films[r][c] = type

## 여러 약품에 대해서 막을 변경
# input : films, D, W, K, medicines
def change_films (films, W, medicines):
    for medicine in medicines:
        r, type =  medicine[0][1]
        change_film(films, r, type, W)

## 백트래킹
# n개를 투여한다고 했을 때, 백트래킹으로 모든 경우 다 해보는 함수
# n개가 됐을 때, 성능검사 통과하는 지 확인
# 재귀 호출 하기 전에 약물을 투여하고 호출문 다음에 롤백
# 입력: D: 두께, n: 남은 투여할 약품 개수
def backtracking(D, n):
    global res
    global success
    if n == 0:

        #### 성능 검사
        # 통과한다면?
        # 전역 변수를 수정한다
        # 아래 트리 확장 단계에서는 success가 이미 true인지 확인하고 탐색
        # 약품 투여 할 필요 없다
        # 지금 단계에서는 이미 n개의 약품이 투여된 상황
        ## 성능검사
        if performance_test(D, W, K, films):
            success = True
        return
    ## 이미 성공했다면 더이상 탐색 안 하도록
    if success == True:
        return
    for i in range(D):
        prev = res[-1][0] if res else -1
        if i > prev:
            # i 번째 막에 A 약품 투여
            temp = films[i][:]
            change_film(films, i, 0, W)
            res.append((i,0))
            backtracking(D, n - 1)
            res.pop()
            ## 원래 대로 롤백
            films[i] = temp

            ## 이미 성공했다면 더이상 탐색 안 하도록
            if success == True:
                return

            # i번째 막에 B약품 투여
            temp = films[i][:]
            change_film(films, i, 1, W)
            res.append((i,1))
            backtracking(D, n - 1)
            res.pop()
            ## 원래 대로 롤백
            films[i] = temp


## 성능검사 함수
# 입력으로 D, W, K, films 받고
# True False 리턴
def performance_test(D, W, K, films):
    # k가 1이라면 탐색 필요 없음
    if K == 1:
        return True
    # 각 열 마다 아래로 내려가면서 연속된 같은 속성 k개 있나 확인
    # 내려가면서 cnt와 prev 값을 갱신
    for c in range(W):
        cnt = 1
        prev = films[0][c]
        for r in range(1, D):
            if films[r][c] == prev:
                cnt += 1
                # cnt 가 K가 됐다면 break
                if cnt >= K:
                    break
            else:
                # 0이 아니라 1로 초기화해야됨
                cnt = 1
                prev = films[r][c]
        # cnt가 K보다 작다면 false
        # cnt가 K보다 컸다면 바로 break되어서 아래 if문으로 왔을 것이므로
        if cnt < K:
            return False

    # 모든 위치 통과하면 true
    return True

## 백트래킹용 전역변수들 초기화 하는 함수
def init():
    global res, visited, success
    res = []
    visited = [False] * D
    success = False

def solution(D, W, K, films):
    ### 현재 상태에서 성능검사 (약품 0)
    if performance_test(D,W,K, films):
        return 0
    ## 1부터 D에 대해서 백트래킹
    for n in range(1, D+1):
        # 백트래킹용자료구조들 초기화
        init()
        backtracking(D, n)
        # 성공이라면 리턴
        if success:
            return n

if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        D, W, K = map(int, input().split())
        films = []
        for _ in range(D):
            films.append(list(map(int, input().split())))
        ### solution 함수 시작
        answer = solution(D, W, K, films)
        print(f'#{test_case} {answer}')
