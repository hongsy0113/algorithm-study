def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
    time = 0
    
    for i, price in enumerate(prices):
        time += 1
        
        if not stack or stack[-1][0] <= price:
            stack.append((price, time, i))
        else:
            p, t, idx  = stack.pop()
            answer[idx] = 1
            cnt = 1
            while stack:
                if stack[-1][0] <= price:
                    stack.append((price, time, i))
                    break
                p, t, idx  = stack.pop()
                answer[idx] = cnt
                cnt+=1
    while stack:
        p, t, idx = stack.pop()
        answer[idx] = time - t

    return answer

prices = [1,2,3,1]
solution(prices)