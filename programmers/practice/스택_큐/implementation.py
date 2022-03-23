import math

def solution(progresses, speeds):
    answer = []
    remain_days = []
    for i in range(len(progresses)):
        remain_days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    arr = [remain_days[0]]

    for i in range(1, len(remain_days)):
        if remain_days[i] > arr[0]:
            answer.append(len(arr))
            arr = [remain_days[i]]
        else:
            arr.append(remain_days[i])
    answer.append(len(arr))
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))