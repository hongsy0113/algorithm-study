def solution(n):
    dp_set = set([])
    dp_set.add(1)

    # 2부터 n번째 못생기 수가 나올 때까지 탐색한다
    i = 2
    cnt = 1
    while cnt < n:
        # 2의 배수라면 2로 나눈 몫이 못생긴 수라면 못생긴 수다
        if i % 2 == 0:
            if i // 2 in dp_set:
                dp_set.add(i)
                cnt += 1
        elif i % 3 == 0:
            if i // 3 in dp_set:
                dp_set.add(i)
                cnt += 1
        elif i % 5 == 0:
            if i // 5 in dp_set:
                dp_set.add(i)
                cnt += 1
        i += 1
    return i - 1



if __name__ == '__main__':
    n = int(input())
    answer = solution(n)
    print(answer)