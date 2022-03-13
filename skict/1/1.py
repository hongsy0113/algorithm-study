def solution(money, costs):
    answer = 0

    coin = [1, 5, 10, 50, 100, 500]
    final_coin = {1:costs[0]}
    for i in range(1, 6):
        if i % 2 == 0:
            # 큰 단위 동전 사용 가능
            if costs[i] <= 2 * costs[i-1]:
                final_coin[coin[i]] = costs[i]
        else:
            if costs[i] <= 5 * costs[i-1]:
                final_coin[coin[i]] = costs[i]
    ### 
    ##print(final_coin)

    # TODO
    # greedy 알고리즘으로 큰 동전 사용
    # 정렬
    final_coin = sorted(final_coin.items(), key = lambda item: item[0], reverse = True)
    # final_coin = [(100, 50), (50, 35), (5, 4), (1, 1)]
    for i in range(len(final_coin)):
        # 동전이 금액보다 큰 경우는 스킵
        if final_coin[i][0] > money:
            continue
        # 동전이 금액보다 작은 경우
        # 필요한 동전개수 카운트
        count = money // final_coin[i][0]
        # 남은 금액 
        money %= final_coin[i][0]
        # 비용 증가
        answer += count * final_coin[i][1]
        
    return answer

money = 4578
#costs = [2, 11, 20, 100,200,600]
#costs = [1, 4, 99, 35, 50, 1000]
costs = [1, 10, 50, 500, 2500, 25000, 1]

print(solution(money,costs))