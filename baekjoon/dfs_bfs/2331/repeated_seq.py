# 맞았습니다
import sys
import math

def main():
    A, P = map(int, sys.stdin.readline().split())
    D = []
    D.append(0)
    D.append(A)

    i=2
    while True:
				# map을 통해 리스트의 각 원소에 동일 연산 적용
				# 1. D[I-1] 원소를 자릿수를 분리해 리스트로 만들기
        digits = list(map(int, str(D[i-1])))
				# 2. 그 리스트에 P승 연산을 적용하기
        pow_digits = list(map(lambda x: int(math.pow(x, P)), digits))
        
				# 이미 수열에 존재하는 값인지 확인
        if sum(pow_digits) in D:
            result = D.index(sum(pow_digits)) -1 
            break

        D.append(sum(pow_digits))
        i+=1

    print(result)
if __name__ == '__main__':
    main()