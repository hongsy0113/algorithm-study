def solution(food_times, k):

    time = 0
    idx = 0
    n = len(food_times)

    while time < k:
        # idx에 있는 음식을 섭취한다
        food_times[idx] -= 1

        # idx 를 다음으로 옮긴다
        for i in range(1, n):
            idx = (idx + 1) % n
            if food_times[idx] > 0:
                break
            # 모든 음식 다 먹은 상황
            if i == n-1 and food_times[idx] == 0:
                return -1
        # time 증가
        time += 1
    
    return idx+1


food_times = [3,1,2]
k = 5
print(solution(food_times, k))