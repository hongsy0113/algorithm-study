import math
def solution(N, A, B, C):
    cnt = 0
    for i in range(N):
        cnt += math.ceil(((A[i] - B) if A[i]-B>0 else 0)/ C)
    return cnt + N


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    answer = solution(N, A, B, C)
    print(answer)
