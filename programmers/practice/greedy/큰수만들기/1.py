from pandas import concat


def solution(number, k):
    answer = ''
    #num_list = ['4','1','7','7','2','5','2','8','4','1']#list(str(number))
    #answer = ['4','1','7','7','2','5','2','8','4','1']#num_list.copy()
    num_list = list(str(number))
    answer = num_list.copy()
    for i in range(len(num_list)):
        if k == 0 or len(num_list)-i<=k: 
            break
        for num in num_list[i+1:i+k+1]:
            if int(num) > int(num_list[i]):
                answer.remove(num_list[i])
                k -=1
                break
    if k>0:
        answer = num_list[:-k]
    # k >0 이면 뒤에서부터 k개 짜른다
    answer = ''.join(answer)
    return answer


#number=19241
number = 999999999999999
#number=  4177252841
k=10
print(solution(number, k))
