from collections import Counter

def solution(people, limit):
    answer = 0
    people_counter = Counter(people)
    people.sort()
    half = limit // 2
    idx = -1
    for i, p in enumerate(people):
        if p > half:
            idx = i
            break
    ## 전체가 다 small 인 경우
    if idx == -1:
        small_people = people
        big_people = []
    # 전체가 다 big 인 경우
    elif idx == 0:
        small_people = []
        big_people = people
    else:
        big_people = people[idx:]
        small_people = people[:idx]
    big_cnt = len(big_people)
    small_cnt = len(small_people)

    big_people_conter = Counter(big_people)
    # big에서 더이상 더 태울 수 있는지 없는지를 위한 flag
    big_available = True
    for i, small in enumerate(small_people):

        # big_cnt 가 남아있거나 big이 아직 가능하다면
        if big_cnt > 0 and big_available:
            flag = True
            for w in range(limit - small, 39, -1):
                if w in big_people_conter and big_people_conter[w] >= 1:
                    big_people_conter[w] -= 1
                    big_cnt -= 1
                    answer += 1
                    small_cnt -= 1
                    break
                flag = False
            if not flag:
                big_available = False
        if not big_available or big_cnt <= 0:
            break

    # 반복문을 돌고 나면 아직 못탄 사람들의 small_Cnt, big_Cnt 가 남게 되고
    # answer에는 현재까지 사용한 구명보트 수
    print('small_cnt, big_cnt', small_cnt, big_cnt)
    # small 사람들은 둘 씩 태운다
    if small_cnt > 0:
        answer += small_cnt // 2
        answer += 1 if small_cnt % 2 == 1 else 0

    # big 사람들은 한명 씩 태운다
    if big_cnt > 0:
        answer += big_cnt




    print(answer)
    return answer


if __name__ == '__main__':
    people = [70, 50, 80, 50]
    # people = [70, 80, 50]
    # people = [10, 10, 20, 30, 50, 50, 60, 70, 80, 90, 90]
    people = [1, 1, 1, 1, 1, 1, 1, 1]
    limit = 100
    limit = 50
    solution(people, limit)