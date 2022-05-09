def solution(A, B):
    lenA = len(A)
    lenB = len(B)


    insert_cnt = 0
    remove_cnt = 0
    for i in range(lenB):
        if i >= len(A):
            A = A + B[i]
            insert_cnt += 1
        if A[i] == B[i]:
            continue
        else:
            # A.insert(i, B[i])
            A = A[:i] + B[i] + A[i:]
            insert_cnt += 1

    # i가 lenB일때 break 한다
    # len(A)에서 i를 빼면 remove해야할 길이 나옴
    print('A', A)
    remove_cnt = len(A) - i - 1
    print(insert_cnt, remove_cnt)
    answer = 0
    if insert_cnt < remove_cnt:
        answer += insert_cnt
        answer += remove_cnt - insert_cnt
    else:
        answer += remove_cnt
        answer += insert_cnt - remove_cnt
    # if insert_cnt == 0 :
    #     answer = remove_cnt
    # else:
    #     answer = insert_cnt - remove_cnt + 1

    print(answer)

if __name__ == '__main__':
    A = input()
    B = input()
    solution(A, B)