def solution (S):
    count_arr = [0, 0]
    count_arr[int(S[0])] = 1
    for i in range(1,len(S)):
        if S[i-1] != S[i]:
            count_arr[int(S[i])] += 1
    return min(count_arr)


if __name__ == '__main__':
    S = input()
    print(solution(S))