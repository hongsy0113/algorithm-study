import sys 

x = int(sys.stdin.readline())

dp = [0] * (x+1)

dp[1] = 0

for i in range(2, x+1):
    candidate = []
    if i % 5 == 0:
        candidate.append(dp[i//5])
    if i % 3 == 0:
        candidate.append(dp[i//3])
    if i % 2 == 0:
        candidate.append(dp[i//2])
    candidate.append(dp[i-1])

    dp[i] = min(candidate) + 1

print(dp[x])
#print(dp)