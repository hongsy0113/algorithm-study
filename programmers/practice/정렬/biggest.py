# 가장 큰 수
def sort_fun (number):
    if number < 10:
        return (number, number, number)
    elif number <100:
        return (number//10, number % 10, number // 10)
    elif number < 1000:
        return (number//100, (number%100)//10, number % 10)
    else:
        return (1, -1, -1)


# def solution(numbers):
#     answer = ''
#     #numbers.sort(key = lambda x:sort_fun(x), reverse=True)
#     numbers.sort(key = lambda x:sort_fun(x), reverse= True)
#     print(numbers)
#     answer = ''.join(list(map(str, numbers)))

#     return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


numbers = [8, 734, 73, 730]
numbers = 	[1000, 999, 0, 0, 1, 100]
print(solution(numbers))