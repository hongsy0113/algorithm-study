import sys

## 일반좌석을 가진 연속된 n명의 사람들이 앉을 수 있는 경우의 수 구하는 함수
def get_dp(n):
    dp = [1]* (n+1)
    
    if n==1:
        return [0, 1]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

def solve(arr):
    answer = 1
    # 연속된 일반 입장권 사람 수 세는 변수
    count = 0
    slice_list = []
    for i in range(1, len(arr)):
        if arr[i] != -1 :
            count += 1
            if i == len(arr)-1:
                slice_list.append(count)
        else:
            if count>0: slice_list.append(count)
            count = 0

    if not slice_list:
        return 1
    dp = get_dp(max(slice_list))

    for i in range(len(slice_list)):
        answer *= dp[slice_list[i]]

    return answer

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    arr = [i for i in range(n+1)]

    for _ in range(m):
        arr[int(sys.stdin.readline())] = -1

    print(solve(arr))
