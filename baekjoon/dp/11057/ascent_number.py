def solve():
    n = int(input())
    if n == 1:
        return 10
        
    # dp[N][a]
    # N : 수의 자릿수 - 1 을 의미
    # a : 시작하는 숫자(제일 앞자리 수) 를 의미
    dp = [[0]*10 for _ in range(n+1)]
    dp[1] = [1,1,1,1,1,1,1,1,1,1]
    
    for i in range(2, n+1):
        for a in range(10):
            dp[i][a] = sum(dp[i-1][a:10]) % 10007

    return sum(dp[n]) % 10007

if __name__ == '__main__':
    print(solve())