import math
from itertools import permutations

prime = []

def is_prime(num):
    if num == 1 or num==0: return False
    if num in prime: return True
    value = int(math.sqrt(num))
    for n in range(2, value+1):
        if num % n == 0 :
            return False 
    prime.append(num)
    return True

def solution(numbers):
    answer = 0
    digits = list(map(int,numbers))
    digits.sort(reverse= True)
    result=[]
    
    for k in range(1, len(digits)+1):
        for i in permutations(digits, k):
            num = 0
            for j in range(k):
                num += i[j] * (10 ** j)
            if is_prime(num):
                result.append(num)

    answer = len(set(result))
    return answer

print(solution ('011'))