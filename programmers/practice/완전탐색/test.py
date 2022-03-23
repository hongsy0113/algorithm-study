
def solution(answers):
    answer = []
    first_pick = [1,2,3,4,5]
    second_pick = [2,1,2,3,2,4,2,5]
    third_pick = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_count = 5
    second_count = 8
    third_count = 10
    result = [[1, 0], [2, 0], [3,0]]
    for i in range(len(answers)):
        if first_pick[i % first_count] == answers[i]:
            result[0][1] += 1
        if second_pick[i % second_count] == answers[i]:
            result[1][1] += 1
        if third_pick[i % third_count] == answers[i]:
            result[2][1] += 1
    result.sort(key=lambda x:x[1], reverse=True)

    answer = [result[0][0]]
    for i in range(1,len(result)):
        if result[i][1] == result[0][1]:
            answer.append(result[i][0])

    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))