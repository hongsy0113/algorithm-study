def solution(width, height, diagonals):
    answer = 0

    ## 먼저 대각선 없다고 가정하고 2차원 dp 배열 구한다

    dp = [[0 for _ in range(width+1)] for _ in range(height+1)]

    for i in range(height+1):
        for j in range(width+1):
            if i == 0 or j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10000019

    # TODO 대각선들 하나씩 선택해서 경우의 수를 구한다. 
    for diagonal in diagonals:
        # start = (diagonal[0]-1, diagonal[1]-1)
        # end = (diagonal[0], diagonal[1])
        x = diagonal[1]
        y = diagonal[0]
        # TODO 이 대각선을 선택했을 때의 경우의수 
        print("(x, y) = ({}, {})".format(x, y))
        # CASE 1
        ## 왼쪽 아래에서 들어와서 오른쪽 위로 나갈 떄
        # 대각선 시작점 까지의 경우의 수 * 끝점 부터의 경우의 수 * 2
        to_diagonal = dp[x-1][y-1]
        from_diagonal = dp[height-x][width-y]
        answer += to_diagonal * from_diagonal * 2
        answer %= 10000019
        # 꼭 오른쪽위로 나갈 필요 x
        from_diagonal = dp[height-(x+1)][width-(y-1)] if height-(x+1) >= 0 else 0
        answer += to_diagonal * from_diagonal
        from_diagonal = dp[height-(x-1)][width-(y+1)] if height-(y+1) >= 0 else 0
        answer += to_diagonal * from_diagonal
        answer %= 10000019
        # CASE 2
        ## 오른쪽 아래에서 들어와서  나갈 떄
        # 대각선 시작점 까지의 경우의 수 * 끝점 부터의 경우의 수
        to_diagonal = dp[x-2][y] if x-2>=0 else 0
        from_diagonal = dp[height-x][width-(y-1)] 
        answer += to_diagonal * from_diagonal
        answer %= 10000019

        to_diagonal = dp[x][y-2] if y-2>=0 else 0
        from_diagonal = dp[height-(x-1)][width-y] 
        answer += to_diagonal * from_diagonal
        answer %= 10000019

    return answer % 10000019










width = 2
height = 2
diagonals = [[1,1],[2,2]]
print(solution(width, height, diagonals))