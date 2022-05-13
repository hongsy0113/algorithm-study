# 짝지어 제거하기
import time

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

                # 만약 제거가 가능하다면 좌우로 제거 가능한지 본다
                # j가 정의 안 될 때를 대비해서 j 선언
                j = 1

                for j in range(1, max(i+1, len(s) - i - 2)):
                    if i-j < 0 or i + j + 1 >= len(s):
                        break
                    # 좌우 이미 set에 있다면 break
                    if i-j in remove_set or i+ j + 1 in remove_set:
                        break
                    if s[i-j] == s[i+j+1]:
                        remove_set.add(i-j)
                        remove_set.add(i + j + 1)
                    else:
                        break
                i = i + j + 1
                # i += 2
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
    start = time.time()

    print(solution(s))

print('실행시간: ', time.time() - start)