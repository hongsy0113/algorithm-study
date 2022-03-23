def search_count (search_word, goods):
    count = 0
    for i in goods:
        if search_word in i:
            count += 1
    return count

def solution(goods):
    answer = []
    for word in goods:
        answer_per_word = []
        for j in range(1,len(word)+1):
            is_exist = False
            for k in range(len(word)-j+1):
                search_word = word[k:j+k]
                if search_count(search_word,goods) == 1:
                    answer_per_word.append(search_word)
                    is_exist = True
            if is_exist:
                break
        if not is_exist:
            answer_per_word = 'None'
        else:
            answer_per_word = sorted(list(set(answer_per_word)))
            answer_per_word = ' '.join(answer_per_word)
        answer.append(answer_per_word)    
    return answer




goods = ["pencil","cilicon","contrabase","picturelist"]
print(solution(goods))
