import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    house_list = list(map(int, input().split()))

    house_list.sort()
    print(house_list[(N-1)//2])