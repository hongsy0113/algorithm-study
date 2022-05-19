def solution(people, limit):
    answer = 0
    # people을 내림차순 정렬하고 낮은 사람부터 태운다.
    people.sort(reverse=True)
    cur_weight = 0
    answer = 1
    num = 0
    while people:
        weight = people.pop()
        # 한명 더 탈 수 있는 경우
        if weight <= limit - cur_weight and num < 2:
            cur_weight += weight
            num += 1
        # 구명보트 새로 필요한 경우
        else:
            answer += 1
            cur_weight = weight
            num = 1

    print(answer)
    return answer


if __name__ == '__main__':
    people = [70, 50, 80, 50]
    people = [70, 80, 50]
    limit = 100
    solution(people, limit)