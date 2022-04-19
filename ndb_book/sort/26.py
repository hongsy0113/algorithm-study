import sys
from collections import deque
input = sys.stdin.readline

def solution(N, arr):
    answer = 0
    arr.sort(reverse = True)
    while len(arr)>=2:
        # 전체를 정렬시키지 말고 삽입 정렬하듯히 한칸씩 찾아들어가자
        
        first = arr.pop()
        second = arr.pop()
        temp = first+second
        answer += temp
        arr.append(temp)

        if len(arr) <= 1:
            break
        # 삽입 정렬 한 단계
        prev = len(arr)-2
        while prev>=0 and arr[prev] < temp:
            arr[prev+1] = arr[prev]
            prev -= 1
        arr[prev+1] = temp
    return answer 

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    print(solution(N,arr))

