# 짝지어 제거하기
def solution(s):
    if len(s) % 2 == 1:
        return 0
    while s:
        removed = False
        remove_set = set([])
        i = 0
        while i < len(s) - 1:
            # 연속된 두 알파벳이 있을 경우 제거해야한다
            # 제거 인덱스를 set에 추가
            if s[i] == s[i+1]:
                remove_set.add(i)
                remove_set.add(i+1)
                i += 2
            else:
                i += 1

        # 더 이상 제거할 게 없다면 return 0
        if len(remove_set) == 0:
            return 0

        # 제거 후의 s를 새롭게 정의
        length = len(s)
        ns = ''
        for i in range(length):
            if not i in remove_set:
                ns += s[i]
        s = ns

    return 1


if __name__ == '__main__':
    s = 'baabaa'
    s = 'aaaaaaaaaaaaaaaaaaaaaa'
    s = input()
    print(solution(s))