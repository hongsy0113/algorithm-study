import heapq

def solution(jobs):
    answer = 0
    heap = []
    n = len(jobs)
    # 작업을 도착 시간 순으로 정렬
    jobs.sort(key = lambda x: x[0])
    t = 0
    idx = 0
    while True:
        # 도착한 작업들을 전부 우선순위 큐에 넣음
        while idx < n and jobs[idx][0] <= t:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        # 해야할 작업 있다면 처리
        if heap:
            time, come = heapq.heappop(heap)
            # 작업을 처리하면 그 시간만큼 t를 증가
            t += time
            # 해당 작업의 요청으로부터 종료까지 걸린 시간 누적
            answer += t-come
            continue
        # 작업 처리할게 없다면 시간 1씩 증가
        t += 1
        if not heap and idx >= n:
            break
    
    return answer // n