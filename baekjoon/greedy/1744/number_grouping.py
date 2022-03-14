import sys

# TODO : 수열을 음의 정수, 양의 정수, 0으로 분류
def classify_seq(seq):
    negative = []
    positive = []
    zero = []
    one =[]
    for element in seq:
        if element > 1:
            positive.append(element)
        elif element == 0:
            zero.append(element)
        elif element == 1:
            one.append(1)
        else:
            negative.append(element)
    positive.sort(reverse=True)
    negative.sort()
    return positive, negative, zero, one

def solve():
    n = int(sys.stdin.readline())
    seq = []
    sum = 0
    for _ in range(n):
        seq.append(int(sys.stdin.readline()))
    pos, neg, zero, one = classify_seq(seq)

    # 음수가 없다면
    if not neg:
        # 큰 수 두 개씩 짝 짓는다
        pos.sort(reverse=True)
        for i in range(0,len(pos),2):
            if i == len(pos)-1:
                sum+= pos[i]
            else:
                sum += pos[i] * pos[i+1]
        # 1 들은 그냥 더해준다
        sum += len(one)
    ## 음수가 있다면
    else:
        for i in range(0, len(neg), 2):
            # 음수 개수가 홀수라면
            if i == len(neg) -1:
                # 0이 있다면 안 더해도 됨. 0 이 없다면 더한다
                if not zero:
                    sum += neg[i]
            else:
                sum += neg[i] * neg[i+1]
        for i in range(0, len(pos), 2):
            if i == len(pos)-1:
                sum+= pos[i]
            else:
                sum += pos[i] * pos[i+1]
        sum += len(one)
    print(sum)

if __name__ == '__main__':
    solve()