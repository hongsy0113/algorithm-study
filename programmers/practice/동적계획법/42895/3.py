from collections import defaultdict


def solution(N, number):
    # N 1개 사용한 수, 2개 사용한 수, .... number 나올때까지 반복
    # 사용한 N의 개수를 key로 하고 그 개수로 만들 수 있는 숫자들의 set을 value로 하는 dictionary
    dp_dict = defaultdict(set)

    dp_dict[1].add(N)
    if N == number:
        return 1
    # 지금까지 등장한 수 모두 기록하기 위한 set
    total_set = {N}

    # k는 최소 1부터 최대 8
    for k in range(2, 9):
        # N을 k번 concat 한 수 추가
        n = int(str(N) * k)
        if n == number:
            return k
        if not n in total_set:
            dp_dict[k].add(n)
            total_set.add(n)

        ## i = 1 부터 k-1 까지
        # i개 사용한 값들과 k-i 개 사용한 값들과 모든 조합 사칙연산하면 k개 사용한 값이 나온다.
        for i in range(1, k):
            j = k - i
            for v1 in dp_dict[i]:
                for v2 in dp_dict[j]:
                    new_value = v1 + v2
                    if new_value == number:
                        return k
                    if not new_value in total_set:
                        total_set.add(new_value)
                        dp_dict[k].add(new_value)
                    new_value = v1 - v2
                    if new_value == number:
                        return k
                    if not new_value in total_set:
                        total_set.add(new_value)
                        dp_dict[k].add(new_value)
                    new_value = v1 * v2
                    if new_value == number:
                        return k
                    if not new_value in total_set:
                        total_set.add(new_value)
                        dp_dict[k].add(new_value)
                    if v2 == 0:
                        continue
                    new_value = v1 // v2

                    if new_value == number:
                        return k
                    if not new_value in total_set:
                        total_set.add(new_value)
                        dp_dict[k].add(new_value)

    return -1


if __name__ == '__main__':
    N = 7
    number = 7778
    print(solution(N, number))
