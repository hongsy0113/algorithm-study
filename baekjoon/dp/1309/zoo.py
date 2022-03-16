def solve(n):
    if n==1: return 3
    dp= [[0]*3 for _ in range(n)]
    dp[0] = [1, 1, 1]

    for i in range(1, n):
        # i번째 줄에서 사자를 안 넣을 경우
        dp[i][0] = sum(dp[i-1]) % 9901
        # i번째 줄에서 사자를 왼쪽 칸에 넣는 경우
        dp[i][1] = (dp[i-1][2] + dp[i-1][0]) % 9901
        # i번째 줄에서 사자를 오른쪽 칸에 넣는 경우
        dp[i][2] = (dp[i-1][1] + dp[i-1][0]) % 9901
    return sum(dp[n-1]) % 9901

if __name__ == '__main__':
    n = int(input())
    print(solve(n))