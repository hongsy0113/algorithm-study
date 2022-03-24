def solution(brown, yellow):
    answer = []
    
    perimeter = (brown - 4) // 2

    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow // i
            if i+j == perimeter:
                answer = [j+2, i+2]
                break
    
    return answer



brown = 8
yellow = 1
print(solution (brown, yellow))