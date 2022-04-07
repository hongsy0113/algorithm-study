
def solution (num_str):
    result = int(num_str[0])
    for i in range(1, len(num_str)):
        n = int(num_str[i])
        if result == 0:
            result = n
            continue
        if n==0 or n==1:
            result += n
        else:
            result *= n
    
    return result


if __name__ == '__main__':
    examples = ['02984', '567', '765', '20984']
    for e in examples:
        print(solution(e))
