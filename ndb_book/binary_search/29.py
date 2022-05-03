### 교재 참고해서 제출한 코드
# 맞았습니다!!
import sys
input = sys.stdin.readline


def solution(houses, C, N):
    min_gap, max_gap = 1, houses[-1] - houses[0]
    result = None

    while min_gap <= max_gap:
        mid_gap = (min_gap + max_gap) // 2
        value = houses[0]
        cnt = 1
        for i in range(1, N):
            if houses[i] - value >= mid_gap:
                value = houses[i]
                cnt += 1
                if cnt >= C: break
        if cnt < C:
            max_gap = mid_gap - 1
        else:
            min_gap = mid_gap + 1
			# mid_gap으로 설치 가능한 경우에만 result를 갱신해줘야함
            result = mid_gap

    print(result)

if __name__ == '__main__':
    N, C = map(int, input().split())
    houses = []
    for _ in range(N):
        houses.append(int(input()))

    houses.sort()
    solution(houses, C, N)