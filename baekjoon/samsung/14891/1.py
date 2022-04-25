import sys
input = sys.stdin.readline

# gear 문자열과 시계/반시계 방향 여부를 입력으로 받고 회전
def rotate(gear, clockwise):
    if clockwise:
        left = gear[-1]
        right = gear[:-1]
        gear = left + right
    else:
        left = gear[1:]
        right = gear[0]
        gear = left + right
    return gear

# 톱니 정보와 회전 정보를 통해 연쇄적으로 회전되어야 하는 톱니의 번호와 방향 리턴
def cascade_rotate(gears, command):
    result = []
    # 왼쪽 방향으로 톱니 확인
    if command[0] > 1:
        cur_gear, cur_clockwise = command[0], (True if command[1] == 1 else False)
        while cur_gear > 1:
            next_gear = cur_gear - 1
            if gears[next_gear][2] != gears[cur_gear][-2]:
                result.append([next_gear, not(cur_clockwise)])
                cur_gear = next_gear
                cur_clockwise = not cur_clockwise
            else:
                break
    # 오른쪽 방향으로 톱니 확인
    if command[0] < 4:
        cur_gear, cur_clockwise = command[0], (True if command[1] == 1 else False)
        while cur_gear < 4:
            next_gear = cur_gear + 1
            if gears[next_gear][-2] != gears[cur_gear][2]:
                result.append([next_gear, not (cur_clockwise)])
                cur_gear = next_gear
                cur_clockwise = not cur_clockwise
            else:
                break
    return result

# 네 톱니바퀴의 점수의 합을 구하는 함수
def get_score(gears):
    score = 0
    for i in range(1, 5):
        if gears[i][0] == '1':
            score += 2 ** (i-1)
    return score


def solution(gears, K, commands):
    # TODO: commands를 보면서 어떤 톱니를 어느 방향으로 회전해야하는지 저장
    for command in commands:
        # 각 command로 톱니를 회전하면 어떤 다른 톱니들이 회전해야하는지 구한다.
        to_rotate_list = cascade_rotate(gears, command)
        # 추가로 회전해야하는 톱니들 회전
        for to_rotate in to_rotate_list:
            gear_num, clockwise = to_rotate[0], to_rotate[1]
            gears[gear_num] = rotate(gears[gear_num], clockwise)
        # 원래 command에 있는 톱니 회전
        gears[command[0]] = rotate(gears[command[0]], True if command[1] == 1 else False)
    return get_score(gears)


if __name__ == '__main__':
    gears = ['']

    for _ in range(4):
        gears.append(input().rstrip())
    K = int(input())
    commands = []
    for _ in range(K):
        commands.append(list(map(int, input().split())))
    print(solution(gears, K, commands))