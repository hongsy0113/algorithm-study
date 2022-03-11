import sys

n, m = map(int, sys.stdin.readline().split())

money = []

for i in range(n):
    money.append(int(sys.stdin.readline()))

dp = [-1] * (m+1)

for i in range(min(money), m+1):
    if i in money:
        dp[i] = 1
    else:
        candidate = []
        ## 각 화폐단위별로 뺀 금액 기준으로 경우의 수 비교
        for j in money:
            if dp[i-j] >= 1:
                candidate.append(dp[i-j]+1)
        if candidate:
            dp[i] = min(candidate)
        else: dp[i] = -1

print(dp[m])
# print(dp)
