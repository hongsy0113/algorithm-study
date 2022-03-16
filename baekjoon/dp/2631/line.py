import sys

def solve(arr, n):
    dp = [1] * (n+1)
    stay_biggest = [1] * (n+1)
    moving = [[], []]
    if n == 1: return dp
    for i in range(2, n+1):
        
        print(i)
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    
    return dp

if __name__ == '__main__':
    n = int(input())
    arr = [0]
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    dp = solve(arr, n)
    print(dp[n])