import sys 

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, n):
    dp[i] = max(arr[i] + dp[i-2], dp[i-1])

print(dp[n-1])
