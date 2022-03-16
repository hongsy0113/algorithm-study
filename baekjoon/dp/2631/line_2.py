import sys

# 가장 긴 증가하는 부분 수열의 길이를 구하는 함수
def partial_seq(arr):
    dp = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(i-1, 0, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

def solve(arr, n):
    not_moving_num = partial_seq(arr)
    return n - not_moving_num

if __name__ == '__main__':
    n = int(input())
    arr = [0]
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    print(solve(arr, n))
    