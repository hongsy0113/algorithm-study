import sys
sys.setrecursionlimit(10**7)

dx = [0, 1]
dy = [1, 0]


def solve():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    # dp 배열 0으로 초기화
    # 해당 위치로부터 목적지 까지 갈 수 있는 경우의 수를 저장한다
    dp = [[0]*n for _ in range(n)]
    # dp[출발지] = 1
    dp[0][0] =1 
    for i in range(n):
        for j in range(n):
            if i==n-1 and j == n-1:
                return dp[i][j]
            else:
                jump_range = graph[i][j]
                # 오른쪽
                if j + jump_range < n:
                    dp[i][j + jump_range] += dp[i][j]
                if i + jump_range < n:
                    dp[i+ jump_range][j] += dp[i][j]
if __name__ == '__main__':
    print(solve())