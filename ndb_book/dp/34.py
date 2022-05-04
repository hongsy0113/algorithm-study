import sys
input = sys.stdin.readline

def solution(powers, N):
    dp = [1] * N

    for i in range(N):
        for j in range(i-1, -1, -1):
            if powers[j] > powers[i]:
                dp[i] = max(dp[j] + 1, dp[i])

    # max(dp) 에 가장 긴 감소하는 부분 수열의 길이가 들어간다

    print(N - max(dp))

if __name__ == '__main__':
    N = int(input())
    powers = list(map(int, input().split()))

    solution(powers, N)