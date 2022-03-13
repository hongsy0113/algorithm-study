def solution(width, height, diagonals):
    answer = 0

    dp = [[0 for _ in range(width+1)] for _ in range(height+1)]

    for i in range(height+1):
        for j in range(width+1):
            if i == 0 or j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10000019

    for diagonal in diagonals:
        x = diagonal[1]
        y = diagonal[0]
        # CASE 1-1
        to_diagonal = dp[x-1][y-1]
        from_diagonal = dp[height-x][width-y]
        answer += to_diagonal * from_diagonal * 2
        answer %= 10000019
        # CASE 1-2
        from_diagonal = dp[height-(x+1)][width-(y-1)] if height-(x+1) >= 0 else 0
        answer += to_diagonal * from_diagonal
        # CASE 1-2
        from_diagonal = dp[height-(x-1)][width-(y+1)] if height-(y+1) >= 0 else 0
        answer += to_diagonal * from_diagonal
        answer %= 10000019
        # CASE 2
        to_diagonal = dp[x-2][y] if x-2>=0 else 0
        from_diagonal = dp[height-x][width-(y-1)] 
        answer += to_diagonal * from_diagonal
        answer %= 10000019
        # CASE 3
        to_diagonal = dp[x][y-2] if y-2>=0 else 0
        from_diagonal = dp[height-(x-1)][width-y] 
        answer += to_diagonal * from_diagonal
        answer %= 10000019

    return answer % 10000019
