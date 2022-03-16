def solve(n):
    dp = [0] * (n+1)
    dp[1] = 1
    if n == 1: return 1

    dp[2] = 2

    for i in range(3, n+1):
        # 홀수인 경우
        if i % 2 == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i//2] + dp[i-1]) % 1000000000

    return dp[n] % 1000000000
if __name__ == '__main__':
    n = int(input())
    print(solve(n))