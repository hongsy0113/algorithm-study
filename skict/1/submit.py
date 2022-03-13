def solution(money, costs):
    answer = 0

    coin = [1, 5, 10, 50, 100, 500]
    final_coin = {1:costs[0]}
    for i in range(1, 6):
        if i % 2 == 0:
            if costs[i] <= 2 * costs[i-1]:
                final_coin[coin[i]] = costs[i]
        else:
            if costs[i] <= 5 * costs[i-1]:
                final_coin[coin[i]] = costs[i]

    final_coin = sorted(final_coin.items(), key = lambda item: item[0], reverse = True)
    for i in range(len(final_coin)):
        if final_coin[i][0] > money:
            continue
        count = money // final_coin[i][0]
        money %= final_coin[i][0]
        answer += count * final_coin[i][1]
        
    return answer
