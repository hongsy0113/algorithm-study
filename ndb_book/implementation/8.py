def solution(S):
    str_list = []
    int_list = []
    for s in S:
        if s.isalpha():
            str_list.append(s)
        if s.isdecimal():
            int_list.append(int(s))
    str_list.sort()
    str_list.append(str(sum(int_list)))
    print(''.join(str_list))

if __name__ == '__main__':
    solution(input())