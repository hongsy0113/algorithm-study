def solve():
    n = int(input())
    # dp[N][a]
    # N : 수의 자릿수 - 1 을 의미
    # a : 시작하는 숫자(제일 앞자리 수) 를 의미
    if n == 1:
        print(9)
        return 
    dp = [[0]*10 for _ in range(n+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2,n+1):
        for a in range(1, 10):
            ## 첫 자리 1인경우
            if a == 1:
                if i == 2:
                    dp[i][a] = 2
                else:
                    dp[i][a] = (dp[i-1][2] + dp[i-2][1]) % 1000000000
            ## 첫 자리 9인 경우
            elif a==9:
                dp[i][a] = dp[i-1][8]
            else:
                dp[i][a] = (dp[i-1][a-1] + dp[i-1][a+1]) % 1000000000
    print(sum(dp[n][1:10]) % 1000000000)

if __name__ == '__main__':
    solve()