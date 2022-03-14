def solve():
    for i in range(1, 10001):
        is_self_number = True
        for j in range(1, 36):
            num = i - j
            if num <0 : break
            digits = list(map(int,str(num)))
            if sum(digits) == j:
                # 생성자 존재
                is_self_number = False
                break
        if is_self_number: print(i)

if __name__ == '__main__':
    solve()