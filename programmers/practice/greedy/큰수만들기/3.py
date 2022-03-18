def solution(number, k):
    answer = ''

    num_list = list(str(number))
    answer = num_list.copy()
    ## 같은 부분 탐색 여러번 하지 않도록 최대 숫자 기억
    k_list = answer[1:k+1]
    for i in range(len(num_list)):
        if k == 0 or len(num_list)-i<=k: 
            break
        print('k_list', k_list)
        # 지워야 됨
        if max(k_list) > num_list[i]:
            answer.remove(num_list[i])
            
            k -= 1
        else: 
            print(i, k)
            k_list.append(num_list[i+k+1])
        k_list.remove(num_list[i+1])
        # if not is_deleted :
        #     answer.append(num_list[i])
    if k>0:
        answer = num_list[:-k]
    # k >0 이면 뒤에서부터 k개 짜른다
    answer = ''.join(answer)
    return answer


#number=19241
#number = 900000000000000009
#num
number=  4177252841
k=4
# print(solution(number, k))

numbers=[1924, 1231234, 4177252841]
ks = [2,3,4]

for i in range(len(numbers)):
    print(solution(numbers[i], ks[i]))
