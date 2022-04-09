# A에서 해당 알파벳 만들기 위해 필요한 방향키 수 구하는 함수
def up_down_count(s):
    return min(ord(s)-ord('A'), 26-(ord(s)-ord('A')))

# 가장 가까운 A아닌 곳까지의 거리 구하는 함수
def get_next(str, name, cur):
    for i in range(1, len(name)//2+1):
        is_left = str[cur-i] != name[cur-i]
        is_right = str[(cur+i)%len(name)] != name[(cur+i)%len(name)]
        # 만약 가장 가까운 위치까지 가는 방법이 왼쪽, 오른쪽 모두 가능하다면
        # 더 멀리까지 알파벳 확인해본다
        # A아닌 것들이 연달아서 많이 있으면 나중에 돌아서 한번에 주르륵 하는 게 더 빠르므로
        # A아닌 것들이 더 짧게 연속된 방향부터 처리
        if is_left and is_right :
            left, right = 0, 0
            for j in range(i+1, len(name)//2+1):
                if str[(cur+j)%len(name)] != name[(cur+j)%len(name)]:
                    right += 1
                if str[cur-j] != name[cur-j]:
                    left += 1
                
            return i if right<left else -i
        # 왼쪽, 오른쪽 중 한 방향에 가까운 A아닌 글자 있다면 거기까지의 차이 반환
        elif is_left:
            return -i
        elif is_right:
            return i

    return 0

# cur_idx 부터 시작한다
# 맨끝에서 부터 시작하거나 두번째위치부터 시작하거나
def _solution(name,cur_idx):
    answer = 0
    #cur_idx = 0
    # 이미 첫 글자는 완성이 되었다고 가정
    cur_str = name[0] + 'A' * (len(name)-1)
    while True:
        # 현재 커서 글자를 바꾼다
        if cur_str[cur_idx] != name[cur_idx]:
            answer += up_down_count(name[cur_idx])
            cur_str = cur_str[:cur_idx] + name[cur_idx] + cur_str[cur_idx+1:]
            print(cur_str)
            print(f'{up_down_count(name[cur_idx])} 증가')
        # 다음 커서로 이동
        move = get_next(cur_str, name, cur_idx)
        # 만약 이동해야할 거리가 0이라면 글자가 완성된 것
        if move == 0:
            break
        else:
            answer += move if move>= 0 else -move
            cur_idx = (cur_idx + move) % len(name)
    
    return answer

# main solution 함수
# 먼저 첫글자에 대한 처리를 해주고
# 왼쪽으로 먼저 갔을 떄, 오른쪽 먼저 갔을 때 두 경우를 모두 구하고 최소값을 취한다
def solution (name):
    # 먼저 첫글자에 대한 처리
    answer = up_down_count(name[0])
    # 길이가 1이면 바로 리턴
    if len(name) == 1:
        return answer
    # 왼쪽으로 이동하고 시작한 경우, 오른쪽으로 이동하고 시작한 경우 각각 구하고 최소값
    answer += min( _solution(name, 1), _solution(name, -1 % len(name)))
    # 처음 한칸 이동한 것을 고려해서 + 1 
    # 최소값 취해도 0이라면 처음부터 다 A였다는 것이므로 0리턴
    return answer + 1 if answer != 0 else 0