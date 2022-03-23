def solution(prices):
    answer = []
    for i in range(len(prices)):
        value = len(prices)-i-1
        for j in range(i+1, len(prices)):
            if prices[j]< prices[i]:
                value = j-i
                break
        answer.append(value)

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices=prices))