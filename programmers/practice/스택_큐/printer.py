
from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque([(priorities[i], i) for i in range(len(priorities))])
    
    while queue:
        
        v = queue.popleft()
        if v[0] >= max(priorities):
            priorities.remove(v[0])
            answer += 1
            if v[1] == location:
                break
        else:
            queue.append(v)

    
    return answer

priorities =[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))