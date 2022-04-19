import sys, heapq
from collections import deque
input = sys.stdin.readline

def solution(N, arr):
    answer = 0
    
    while len(arr)>=2:

        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        temp = first+second
        answer += temp
        heapq.heappush(arr, temp)

    return answer 

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        heapq.heappush(arr, int(input()))
    print(solution(N,arr))

