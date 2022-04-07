
from collections import Counter

def solution(food_times, k):

    time = 0
    idx = 0
    n = len(food_times)
    # 몇 바퀴 돌았는지 저장
    round_num = 0
    # 남은 음식 개수
    remain_cnt = n
    count_dict = Counter(food_times)

    while k > remain_cnt and k>0:

        k -= remain_cnt
        round_num += 1
        remain_cnt -= count_dict[round_num]

    for i in range(n):
        if k> 0 and food_times[i] <= round_num:
            k -= 1
        if k == 0 and food_times[i]<= round_num:
            return i + 1
        elif k==0 and food_times[i]>round_num:
            continue
        

    return idx+1


food_times = [3,1,2]
k = 5
print(solution(food_times, k))