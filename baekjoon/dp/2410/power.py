# 해당 수가 2의 제곱수인지 확인
# 비트 연산자로 구현 가능
def is_power (n):
    if (n & (n-1)):
        return False
    else:
        return True


def solve(n):
    dp = [0] * (n+1)
    dp[1] = 1
    if n == 1: return 1

    dp[2] = 2
    
    # 1을 사용하지 않고 만들 수 있는 경우의 수 카운트해 각 짝수마다 저장
    no_one_count = [0] * (n//2 + 1)
    no_one_count[1] = 1

    for i in range(3, n+1):
        # 홀수인 경우
        if i % 2 == 1:
            dp[i] = dp[i-1]
            print(f'{i} 는 {dp[i]} 경우')
        else:
            dp[i] = dp[i-2]
            if i == 4:
                dp[4] = 4
                no_one_count[2] = 2
                continue
            # 그 전 짝수의 경우의 수 중 1이 안 들어간 경우 에 더하기 2를 하는 경우 고려
            dp[i] += no_one_count[i//2 - 1]
            no_one_count[i//2] = no_one_count[i//2 - 1]
            # 제곱수라면 추가 경우를 고려
            if is_power(i):
                # 자기 자신인 경우를 더해준다
                dp[i] += 1
                # 1을 쓰지 않은 경우들에 + i//2를 해주는 경우도 고려
                dp[i] += no_one_count[i//2//2]
                # 1을 사용하지 않는 경우의 수가 2배 + 1로 늘어남(1은 자기 자신)
                no_one_count[i//2] = (no_one_count[i//2 - 1] + no_one_count[i//2//2] + 1)%1000000000
            
            dp[i] %= 1000000000
            print(f'{i}는\n1포함 = {dp[i]-no_one_count[i//2]}  1미포함 = {no_one_count[i//2]}')
   
    return dp[n] % 1000000000
if __name__ == '__main__':
    n = int(input())
    print(solve(n))