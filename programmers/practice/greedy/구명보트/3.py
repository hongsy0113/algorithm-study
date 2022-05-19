
def solution(people, limit):
    answer = 0

    people.sort()

    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1

    return answer

if __name__ == '__main__':

    people = [70, 50, 80, 50]
    limit = 100

    solution(people, limit)