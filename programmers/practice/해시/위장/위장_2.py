def solution(clothes):
    
    cloth_hash = defaultdict(int)
    
    for [c_name, c_type] in clothes:
        cloth_hash[c_type] += 1
    answer = 1
    for key, value in cloth_hash.items():
        # 해당 옷 종류 개수 + 안 입은 경우
        answer *= (value + 1)
    
    
    return answer - 1