def solution(number, k):
    answer = ''
    #num_list = ['4','1','7','7','2','5','2','8','4','1']#list(str(number))
    #answer = ['4','1','7','7','2','5','2','8','4','1']#num_list.copy()
    num_list = list(str(number))
    answer = num_list.copy()
    max_digit = max(answer[1:k+1])
    for i in range(len(num_list)):
        if num_list[i] == '9':
            continue
        if k == 0 or len(num_list)-i<=k: 
            break
        # 지워야하는 경우
        if num_list[i] < max_digit or num_list[i] == '0':
            answer.remove(num_list[i])
            k-=1
            continue
        if num_list[i] >= max_digit or num_list[i] == '9':
            max_digit = max(num_list[i+2: i+k+2])
    if k>0:
        answer = num_list[:-k]
    # k >0 이면 뒤에서부터 k개 짜른다
    answer = ''.join(answer)
    return answer


numbers=[1924, 1231234, 4177252841, 1000000000000, 987654321, 122334567890, 111111]
ks = [2,3,4, 6, 4, 4, 3]

for i in range(len(numbers)):
    print(solution(numbers[i], ks[i]))
