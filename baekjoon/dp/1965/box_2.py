import sys

## idx번째 원소보다 왼쪽에 있는 원소들 중 arr[idx] 보다 작은 원소들 중 dp 값이 최대인 인덱스 반환
def get_index(arr, idx, dp):
    v = 0
    result = -1
    for i in range(idx, -1, -1):
        if arr[i] < arr[idx]:
            if dp[i] > v:
                v= dp[i]
                result = i
    return result

def solve(n, arr):
    if n==1: return 1
    
    # 최대 상자개수 담는 dp 배열
    dp = [0] * n

    dp[0] = 1

    for i in range(1, n):
        idx = get_index(arr, i, dp)
        if arr[i]!=arr[i-1]:
            dp[i] = dp[idx]+1
        else:
            # 값이 이전과 같을 경우는 그대로 유지
            dp[i] = dp[i-1]

    return max(dp)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solve(n, arr)) 