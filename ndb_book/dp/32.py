import sys
input = sys.stdin.readline




def solution(triangle, n):
    dp = [[0] * (i+1) for i in range(n)]

    # 첫 행의 dp 값을 저장해준다
    dp[0][0] = triangle[0][0]

    # 각 행마다 dp 값을 저장한다다
    for r in range(1, n):
        # 각 열에 대해서 해당 숫자를 선택했을 때 가능한 최대갑 갱신
        for c in range(r+1):
            # 이전 행에서 선택할 수 있는 값들을 list로 만든다
            candidates = []
            # 맨 오른쪽 수의 경우는 자신의 열번호에 해당하는 값이 그전 행에 없다
            if c < r:
                candidates.append(dp[r-1][c])
            # 맨 왼쪽 수는 자신의 열번호 - 1 에 해당하는 값이 그전 행에 없다.
            if c-1>=0:
                candidates.append(dp[r-1][c-1])

            dp[r][c] = triangle[r][c] + max(candidates)


    print(max(dp[-1]))



if __name__ == '__main__':
    n = int(input())
    # 삼각형을 각 원소의 길이가 다른 2차원 리스트로 구현
    triangle = []
    for i in range(n):
        triangle.append(list(map(int, input().split())))

    solution(triangle, n)
