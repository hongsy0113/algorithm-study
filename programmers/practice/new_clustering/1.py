## TODO : 다중집합 만드는 함수
def to_set(str):
    str_set = {}
    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            element = str[i:i+2].lower()
            if element in str_set:
                str_set[element] += 1
            else:
                str_set[element] = 1
    return str_set

#TODO : 자카드 유사도 구하는 함수
def jaccard_similarity(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1
    
    # 합집합
    union = set_a.copy()
    for key, value in set_b.items():
        if key in union:
            union[key] = max(union[key], set_b[key])
        else:
            union[key] = value
    union_len = sum(union.values())

    intersection_len = 0 
    for key in set_a:
        if key in set_b:
            intersection_len += min(set_a[key], set_b[key])
    return intersection_len / union_len

def solution(str1, str2):
    answer = 0

    set_a = to_set(str1)
    set_b = to_set(str2)
    answer = jaccard_similarity(set_a, set_b)

    return int(answer * 65536)

print(solution('FRANCE', 'french'))