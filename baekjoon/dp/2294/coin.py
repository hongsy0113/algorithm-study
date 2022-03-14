import sys

def solve():
    MAX = 10001
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()) )
    coins.sort()

    dp = [MAX] * (k+1)

    for i in range(1, k+1):
        # i가 가장 작은 동전 금액보다 작다면 방법 x
        if i < coins[0]:
            dp[i] = MAX
            continue
        
        if i in coins:
            dp[i] = 1
        else:
            for coin in coins:
                if i-coin >=1:
                    dp[i] = min(dp[i], 1+dp[i-coin])
    
    return dp[k] if dp[k]<MAX else -1
if __name__ == '__main__':
    print(solve())