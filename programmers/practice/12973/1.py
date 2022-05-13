# 짝지어 제거하기
def solution(s):
    while s:
        removed = False
        for i in range(len(s)-1):
            # 연속된 두 알파벳이 있을 경우 제거
            if s[i] == s[i+1]:
                left = s[:i]
                right = s[i+2:]
                s = left + right

                removed = True
                break
        if not removed:
            return 0
    return 1


if __name__ == '__main__':
    s = 'baabaa'
    s = 'aaaaaaaaaaaaaaaaaaaaaa'
    s = input()
    print(solution(s))