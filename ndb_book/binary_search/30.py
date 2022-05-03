from bisect import bisect_left, bisect_right


def solution(words, reversed_words,queries):
    answer = []

    ## 모든 쿼리에 대해서 반복
    for query in queries:
        # 와일드카드가 접두사인지 접미사인지 확인
        if query[-1] == '?':
            # 접미사라면 words 사용
            # 와일드카드 처음 등장하느 idx 찾는다
            for i in range(1, len(query)):
                if query[i] == '?':
                    idx = i
                    break
            # 와일드카드 제거된 앞부분을 query1
            query1 = query[:idx]
            # 와일드카드에 zz 를 대입한 단어를 query2
            zz = 'z' * (len(query) - idx)
            query2 = query1 + zz

            # 탐색해야할 위치 정한다
            start = bisect_left(words, query1)
            end = bisect_right(words, query2)
            length = len(query)
            cnt = 0
            # 후보들 중 길이 일치하면 cnt 증가
            for i in range(start, end, 1):
                if len(words[i]) == length:
                    cnt += 1
            answer.append(cnt)
        # 접두사가 와일드카드라면 reversed_words 사용
        else:
            # 와일드카드 아닌 문자 처음 등장하는 idx 찾는다
            for i in range(1, len(query)):
                if query[i] != '?':
                    idx = i
                    break
            query1 = ''.join(reversed(query[idx:]))
            zz = 'z' * idx
            query2 = query1 + zz

            # 탐색해야할 위치 정한다
            start = bisect_left(reversed_words, query1)
            end = bisect_right(reversed_words, query2)
            length = len(query)
            cnt = 0
            # 후보들 중 길이 일치하면 cnt 증가
            for i in range(start, end, 1):
                if len(reversed_words[i]) == length:
                    cnt += 1
            answer.append(cnt)
    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    reversed_words = [''.join(reversed(word)) for word in words]

    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    words.sort()
    reversed_words.sort()
    print(reversed_words)
    print(solution(words, reversed_words, queries))