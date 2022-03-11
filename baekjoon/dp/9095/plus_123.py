import sys

T = int(sys.stdin.readline())

n_list = []

for i in range(T):
    n_list.append(int(sys.stdin.readline()))

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

# dp 테이블 계산
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 결과 출력
for n in n_list:
    print(dp[n])