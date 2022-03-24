#완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    completion_dict = {}
    for player in completion:
        if player in completion_dict:
            completion_dict[player] += 1
        else:
            completion_dict[player] = 1
    
    for player in participant:
        if not player in completion_dict:
            return player
        elif completion_dict[player] <= 0:
            return player
        else:
            completion_dict[player] -= 1
    return answer

### 참고 답안
import collections
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

solution2(participant, completion)