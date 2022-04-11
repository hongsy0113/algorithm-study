from audioop import reverse


def _solution(n,gap_list, dist):
    pass


def solution(n, weak, dist):
    answer = 0

    dist.sort(reverse=True)
    gap_list = []

    for i in range(len(weak)):
        gap = weak[(i+1) % len(weak)] - weak[i]
        gap_list.append(gap % n)
    # gap_list = [weak[(i+1) % len(weak)] - weak[i] for i in range(len(weak))]
    print(gap_list)

    for i, d in enumerate(dist):
        cnt = 0
        for j in range(len(gap_list)):
            
        pass
    return answer


n = 12
weak = [ 1, 5, 6, 10]
dist = [1,2,3,4]

solution(n, weak, dist)