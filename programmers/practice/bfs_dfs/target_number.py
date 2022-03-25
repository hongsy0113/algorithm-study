from collections import deque

def bfs(numbers, target):
    queue = deque([(numbers[0], 0), (-numbers[0], 0)])
    count = 0
    while queue:
        num, idx = queue.popleft()
        if idx == len(numbers)-1:
            break
        if idx == len(numbers) -2 :
            if num + numbers[idx+1] == target:
                count += 1
            if num - numbers[idx+1] == target:
                count += 1
        queue.append((num + numbers[idx+1], idx+1))
        queue.append((num - numbers[idx+1], idx+1))

    return count



def solution(numbers, target):
    answer = (bfs(numbers, target))
    return answer

numbers = [4, 1, 2, 1]
target = 4
solution(numbers, target)