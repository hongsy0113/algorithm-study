def solve(n):
    dp = [0, 1, 1]
    if n <= 2:
        return dp[n]
    for i in range(3, n+1):
        # dp [i] = dp[i-1] + dp[i-2]
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(solve(n))