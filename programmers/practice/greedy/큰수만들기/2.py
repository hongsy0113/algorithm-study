from pandas import concat


def solution(number, k):
    answer = ''
    #num_list = ['4','1','7','7','2','5','2','8','4','1']#list(str(number))
    #answer = ['4','1','7','7','2','5','2','8','4','1']#num_list.copy()
    num_list = list(str(number))
    answer = num_list.copy()
    for i in range(len(num_list)):
        is_deleted = False
        if num_list[i] == '9':
            continue
        if k == 0 or len(num_list)-i<=k: 
            break
        for num in num_list[i+1:i+k+1]:
            if int(num) > int(num_list[i]) or num_list[i] =='0':
                answer.remove(num_list[i])
                k -=1
                break
        # if not is_deleted :
        #     answer.append(num_list[i])
    if k>0:
        answer = num_list[:-k]
    # k >0 이면 뒤에서부터 k개 짜른다
    answer = ''.join(answer)
    return answer


#number=19241
number = 900000000000000009
#num
# ber=  4177252841
k=13
print(solution(number, k))
