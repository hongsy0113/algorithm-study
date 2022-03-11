import sys

def main():
    n = int(sys.stdin.readline())
    p_list = list(map(int, sys.stdin.readline().split()))
    p_list.sort()

    arr = [0] * n
    arr[0] = p_list[0]
    for i in range(1, n):
        arr[i] = arr[i-1] + p_list[i]
    print(sum(arr))

if __name__ == '__main__':
    main()