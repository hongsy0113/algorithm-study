from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([])
    queue_wait = deque(truck_weights)
    time = 0
    finished_count = 0
    idx = 0
    while True:
        time += 1

        if queue and queue[0][1] == time:
            queue.popleft()
            finished_count += 1
        if queue_wait:
            if len(queue) == 0 or queue_wait[0] <= weight - sum([q[0] for q in queue]):
                queue.append((queue_wait.popleft(), time + bridge_length))
        
        if len(queue_wait) == 0:
            return queue[-1][1]

    return time+1






bridge_length = 2 
weight = 10
truck_weights= [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))