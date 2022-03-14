import sys

def solve():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys.stdin.readline()) )
    coins.sort()

    dp = [0] * (k+1)

    for coin in coins:
        for i in range(k+1):
            # 동전 금액이랑 일치하는 금액은 dp ++
            if i == coin:
                dp[i] += 1
            # i가 동전보다 작으면 변화가 없음
            elif i < coin:
                continue
            # i가 동전보다 크면 dp[i-coin]을 확인
            else:
                dp[i] += dp[i-coin]
    return dp[k]

if __name__ == '__main__':
    print(solve())