# 해당 그룹이 모집 끝낼 수 있는지 확인
# 현재 그룹원 중 공포도 최대인 사람, 그룹원 수를 바탕으로
# 제일 뒤에 원소가 공포도 최대라고 가정
def is_complete (group):
    max_value = group[-1]
    if max_value <= len(group):
        return True
    else:
        return False

def solution(people):
    people.sort()

    temp_group = []
    answer = 0

    # 순서대로 한명씩 임시 그룹에 넣는다
    # 그룹이 완성됐다면 count를 증가시키고 임시 그룹을 비운다.
    for p in people:
        temp_group.append(p)
        if is_complete(temp_group):
            answer += 1
            temp_group = []
    
    return answer

if __name__ == '__main__':
    N = int(input())
    people = list(map(int, input().split()))
    print(solution(people))