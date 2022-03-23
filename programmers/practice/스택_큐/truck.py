from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue_on_bridge = deque([0] * bridge_length)
    queue_wait = deque(truck_weights)
    time = 0
    finished_count = 0
    idx = 0
    while True:
        time += 1
        # pop 했는데 0 아니라면 트럭이 다리를 지난 것이므로 count 증가
        v = queue_on_bridge.popleft()
        if v >0:
            finished_count += 1
        if idx < len(truck_weights) and truck_weights[idx] <= weight - sum(queue_on_bridge):
            queue_on_bridge.append(truck_weights[idx])
            idx += 1
        else:
            queue_on_bridge.append(0)
        if finished_count == len(truck_weights):
            break

    return time






bridge_length = 100
weight = 100
truck_weights= 	[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))