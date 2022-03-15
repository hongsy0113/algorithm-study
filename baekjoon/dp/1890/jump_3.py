import sys
sys.setrecursionlimit(10**7)

dx = [0, 1]
dy = [1, 0]

def search(x, y):
    if x== n-1 and y == n- 1:
        return 1
    #print(x,y)
    jump_range = graph[x][y]
    if jump_range == 0:
        dp[x][y]=-1
        return 0
    for i in range(2):
        nx = x + jump_range * dx[i]
        ny = y + jump_range * dy[i]
        if 0<=nx<n and 0<=ny<n:
            # 다음 위치의 dp 값이 0보다 클 경우 이미 계산된 값이므로 추가 계산 필요 x
            if dp[nx][ny] > 0 :
                dp[x][y] += dp[nx][ny]
            elif dp[nx][ny] == -1:
                continue
            else: 
            # 다음 위치의 dp 값을 알기 위해 해당 위치에서 search 시작
                dp[x][y] += search(nx, ny)
    # 만약 모든 탐색을 마치고도 경우의 수가 0이라면 해당 위치에서는 목적지로 갈 수 없다는 뜻
    if dp[x][y] == 0: 
        dp[x][y] = -1
    
    return dp[x][y] if dp[x][y] != -1 else 0

def solve():
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    search( 0, 0)
    print(dp[0][0] if dp[0][0] != -1 else 0)
if __name__ == '__main__':
    n = int(input())
    graph = []
    # dp 배열 0으로 초기화
    # 해당 위치로부터 목적지 까지 갈 수 있는 경우의 수를 저장한다
    dp = [[0]*n for _ in range(n)]
    # dp[목적지] = 1 
    dp[n-1][n-1] = 1 
    solve()