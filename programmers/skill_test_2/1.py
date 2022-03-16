def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    print(people)

    cur_limit = limit

    i = 0
    j = len(people)-1
    while True:
        if i >j: break
        
        # 현재 가장 무거운 사람 태운다.
        answer += 1
        cur_limit = limit - people[i]
        # 그런 다음 작은 사람순서대로 빈 공간에 태운다
        while cur_limit >=0:
            if  people[j] <= cur_limit:
                cur_limit -= people[j]
                j -= 1
            else:
                break
        
        i += 1

    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution (people, limit))