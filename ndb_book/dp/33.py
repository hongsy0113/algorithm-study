import sys
input = sys.stdin.readline


def solution(N, T, P):
    dp = [0] * N

    # 점화식
    # dp[i] = max(P[i] + dp[i+T[i]], dp[i+1])
    # dp[i] = max(A, B)

    for i in range(N-1, -1, -1):
        B = dp[i+1] if i+1 < N else 0

        # 자신을 선택할 수 없는 경우
        if i + T[i] > N:
            A = 0
        # 자기 자신 선택할 수 있지만 그러면 더이상 다른 상담 못 선택하는 경우
        elif i + T[i] == N:
            A = P[i]
        else:
            A = P[i] + dp[i + T[i]]

        dp[i] = max(A, B)
    print(dp[0])

if __name__ == '__main__':
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)


    solution(N, T, P)
