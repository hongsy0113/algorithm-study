import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) < 2: 
            answer = -1
            break
        first_food = heapq.heappop(scoville)
        second_food = heapq.heappop(scoville)
        new_food = first_food + (second_food * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer