from collections import defaultdict
from itertools import combinations

def solution(clothes):
    # 종류 하나만 입은 경우
    answer = len(clothes)
    
    cloth_hash = defaultdict(int)
    
    for [c_name, c_type] in clothes:
        cloth_hash[c_type] += 1
    
    # 종류 전체 다 입은 경우
    
    if len(cloth_hash)> 1:
        v = 1
        for type, cnt in cloth_hash.items():
            print(type, cnt)
            v *= cnt
        #print(v)
        answer += v
    #print(len(cloth_hash))
    #print(list(cloth_hash.keys()))
    if len(cloth_hash) > 1:
        for i in range(2, len(cloth_hash)):
            comb = combinations(cloth_hash.keys(), i)
            for data in comb:
                cases = 1
                for j in range(i):
                    cases *= cloth_hash[data[j]]
                answer += cases
    return answer