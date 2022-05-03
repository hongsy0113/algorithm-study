def bsearch(arr, l, r):
    if l <= r:
        mid = (l + r) // 2
        value = arr[mid]
        if value == mid:
            print(value)
            return
        elif value < mid:
            bsearch(arr, mid+1, r)
        else:
            bsearch(arr, l, mid - 1)

    else:
        print(-1)
        return

def solution(arr, N):
    bsearch(arr, 0, N-1)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    solution(arr, N)