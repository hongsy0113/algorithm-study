def solution(s):
    answer = 1000
    if len(s) == 1: return 1
    for k in range(1, len(s)//2 + 1):
        length = 0
        temp = s[0:k]
        count = 1
        for i in range(k, len(s),k):
            if len(s[i:i+k]) < k:
                length += len(s[i:i+k])
            elif s[i:i+k] == temp:
                count += 1
            else:
                temp = s[i:i+k]
                length += k + (len(str(count)) if count > 1 else 0)
                count = 1
        length += k + (len(str(count)) if count > 1 else 0)
        answer = min(answer, length)
    return answer

s = "aabbaccc"
solution(s)