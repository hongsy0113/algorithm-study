import sys
input = sys.stdin.readline

N, x = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = N-1

count = 0

def binary_search(arr, left, right, key, cnt):
    global count
    print(f"binary_search({left},{right},{key},{cnt})")
    if left<=right:
        mid = (left+right) // 2

        if key < arr[mid]:
            binary_search(arr, left, mid-1, key, cnt)
        elif key > arr[mid]:
            binary_search(arr, mid+1, right, key, cnt)
        else:
            count += 1
            binary_search(arr, left, mid-1, key, 0)
            binary_search(arr, mid+1, right, key, 0)

binary_search(arr, left, right, x, 0)
print(count if count >0 else -1)