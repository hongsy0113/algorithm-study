from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(words, queries):
    answer = []

    reversed_words = [''.join(reversed(word)) for word in words]
    words.sort()
    reversed_words.sort()
    words_dict = defaultdict(list)
    reversed_words_dict = defaultdict(list)
    for i in range(len(words)):
        words_dict[len(words[i])].append(words[i])
        reversed_words_dict[len(reversed_words[i])].append(reversed_words[i])

    ## 모든 쿼리에 대해서 반복
    for query in queries:
        length = len(query)
        ### 전체가 다 ?인지 확인
        if query == '?' * length:
            # 그렇다면 dict 에서 해당 길이에 해당하는 리스트의 길이 리턴
            answer.append(len(words_dict[length]))
            continue

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
            start = bisect_left(words_dict[length], query1)
            end = bisect_right(words_dict[length], query2)
            cnt = 0
            # 후보들 중 길이 일치하면 cnt 증가
            for i in range(start, end, 1):
                if len(words_dict[length][i]) == length:
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
            start = bisect_left(reversed_words_dict[length], query1)
            end = bisect_right(reversed_words_dict[length], query2)
            cnt = 0
            # 후보들 중 길이 일치하면 cnt 증가
            for i in range(start, end, 1):
                if len(reversed_words_dict[length][i]) == length:
                    cnt += 1
            answer.append(cnt)
    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    reversed_words = [''.join(reversed(word)) for word in words]

    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    words.sort()
    reversed_words.sort()
    solution(words,  queries)