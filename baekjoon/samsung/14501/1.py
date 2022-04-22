import sys
input = sys.stdin.readline

def solution(T, P, N):
    # 동적프로그래밍 사용
    dp = [0] * (N+1)
    # 뒤에서부터 dp 리스트 갱신
    for i in range(N, 0, -1):
        # N+1일째에는 회사에 없다.
        if i + T[i] - 1 > N:
            dp[i] =0

        # 점화식
        #dp[i] = max(dp[i+1], p[i] + dp[i+t[i]-1])
        # dp[i] = max(a, b)
        a = dp[i+1] if i < N else 0
        # 해당 작업을 선택할 수 없는 경우
        if i + T[i] > N + 1:
            b = 0
        # 해당 작업을 선택하면 더이상 못 고르는 경우
        elif i + T[i] == N + 1:
            b = P[i]
        else:
            b = P[i] + dp[i+T[i]]
        dp[i] = max(a, b)

    return dp[1]

if __name__ == '__main__':
    N = int(input())
    T = [-1]
    P = [-1]
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    print(solution(T, P, N))