import sys

def get_index(min_list, a):
    for i in range(len(min_list)-1, 0, -1):
        if min_list[i] > a:
            return i
    return -1

def solve(n, arr):
    if n==1: return 1
    ## 뒤에서부터 하기위해서 reverse
    arr.reverse()
    # 최대 상자개수 담는 dp 배열
    dp = [0] * n
    # 최대 상자 개수 담았을 때 가장 작은 상자의 크기
    min_list = [0] * n
    dp[0] = 1
    min_list[0] = arr[0]
    for i in range(1, n):
        # 기본적으로 i번쨰 원소를 안 담으면 
        dp[i] = dp[i-1]
        min_list[i] = min_list[i-1]

        if arr[i] < min_list[i-1]:
            dp[i] = max(dp[i], dp[i-1]+1)
            min_list[i] = arr[i]
        else:
            # TODO i번째 원소가 min을 처음으로 차지하는 index를 찾자.
            if arr[i] >= max(min_list):
                if dp[i-1] <=1 :
                    dp[i]=1
                    min_list[i] = arr[i]
            else:
                idx = get_index(min_list, arr[i])
                if dp[idx]+1 > dp[i]:
                    dp[i] = dp[idx]+1
                    min_list[i] = arr[i]
                #dp[i] = max(dp[i], dp[idx]+1)
    return dp[-1]       

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solve(n, arr)) 