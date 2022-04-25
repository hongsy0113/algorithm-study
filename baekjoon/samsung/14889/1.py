import sys
input = sys.stdin.readline
INF = 999999
# 조합함수
def get_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        v = arr[i]
        rest_part = arr[i+1:]
        for C in get_combinations(rest_part, n-1):
            result.append([v]+C)
    return result

def get_score(s, team):
    score = 0
    for player1 in team:
        for player2 in team:
            if player1 == player2:
                continue
            score += s[player1-1][player2-1]
    return score

def solution(s):
    N = len(s)
    players = [i for i in range(1, N+1)]
    min_value = INF
    # 먼저 모든 경우의 수로 팀을 짜보고 능력치를 비교
    for it in get_combinations(players, N//2):
        start = []
        link = []
        # 두 팀으로 나눈다.
        for player in players:
            if player in it :
                start.append(player)
            else:
                link.append(player)
        # 능력치의 차이를 구한다
        value = abs(get_score(s, start) - get_score(s, link))
        # 최소값 갱신
        if value < min_value:
            min_value = value
    return min_value


if __name__ == '__main__':
    N = int(input())
    s = []
    for _ in range(N):
        s.append(list(map(int, input().split())))
    answer = solution(s)

    print(answer)