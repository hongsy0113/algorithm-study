def solution(N, number):
    # N 1개 사용한 수, 2개 사용한 수, .... number 나올때까지 반복
    # 사용한 N의 개수를 key로 하고 그 개수로 만들 수 있는 숫자들의 set을 value로 하는 dictionary
    dp_dict = {}

    dp_dict[1] = {N}

    # 지금까지 등장한 수 모두 기록하기 위한 set
    total_set = {N}

    # k는 최소 1부터 최대 8
    for k in range(2, 9):
        print(f'k = {k}------------------')
        # N을 k번 concat 한 수 추가
        n = int(str(N) * k)
        if n == number:
            return k
        dp_dict[k] = {n}
        total_set.add(n)
        ## dp_dict[k-1]에 있는 수들에 5를 더하고, 곱하고, 빼고, 나눈 수들 고려
        # 해당 수가 number인지 확인하는 과정 필요
        # 해당 수가 중복으로 등장한 값은 아닌지 확인하는 과정 필요
        for value in dp_dict[k - 1]:
            print(value)
            # 더하기
            n = value + N
            if n == number:
                return k
            if not n in total_set and n >= 1:
                dp_dict[k].add(n)
                total_set.add(n)
            # 빼기
            n = value - N
            if n == number:
                return k
            if not n in total_set and n >= 1:
                dp_dict[k].add(n)
                total_set.add(n)
            # 곱하기
            n = value * N
            if n == number:
                return k
            if not n in total_set and n >= 1:
                dp_dict[k].add(n)
                total_set.add(n)
            # 나누기
            # 나누어떨어져야지만 가능
            if value % N != 0:
                continue
            n = value // N
            if n == number:
                return k
            if not n in total_set and n >= 1:
                dp_dict[k].add(n)
                total_set.add(n)
    return -1


if __name__ == '__main__':
    N = 5
    number = 12
    print(solution(N, number))
