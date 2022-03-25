def solution(N):
    length = len((N))//2
    n_list = list(map(int, (N)))
    if sum(n_list[:length]) == sum(n_list[length:]):
        print('LUCKY')
    else:
        print('READY')

if __name__ == '__main__':
    solution((input()))