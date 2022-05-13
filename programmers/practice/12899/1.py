
# 1은 1, 2는 2, 0은 4로 매핑하는 함수
def to_124(num):
    if num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 0:
        return '4'

    return -1

def solution(n):
    answer = ''

    # n을 3으로 나눈 나머지를 통해 맨 뒷자리 수를 알아낸다
    # n = (n-1) //3 을 하고 위 과정을 반복한다

    while True:
        num = n % 3
        answer += to_124(num)
        n = (n - 1) // 3
        if n == 0:
            break
    answer = ''.join(reversed(answer))
    return answer

if __name__ == '__main__':
    n = int(input())
    solution(n)