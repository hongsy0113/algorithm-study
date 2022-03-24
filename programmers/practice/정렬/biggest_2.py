# 가장 큰 수
from itertools import permutations

def solution(numbers):
    answer = ''
    max_value = 0
    for i in permutations(numbers, len(numbers)):
        max_value = max(int(''.join(list(map(str, list(i))))), max_value)
    answer = str(max_value)
    return answer

numbers = [8, 734, 73, 730]
print(solution(numbers))