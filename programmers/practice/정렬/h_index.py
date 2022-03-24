def solution(citations):
    answer = 0
    citations.sort(reverse= True)
    print(citations)
    n = len(citations)
    for i, citation in enumerate(citations):

        if i+1 >= citation:
            return citation

    return answer

citations = [3, 0, 6, 1, 5]
citations = [6, 6, 6, 6, 6]
print(solution(citations))