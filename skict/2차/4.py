
def get_candidate(n, m, k, record):
    candidate = []

    keys = sorted(list(set(record)))

    if len(keys) == k:
        temp_list = [-1] +sorted(list(set(record.copy())))
        for i in range(len(record)):
            candidate.append(temp_list.index(record[i]))
        
        return [tuple(candidate)]
    cases = []
    for i in range(1, len(keys)+2):
        if i == 1 and 1 in record:
            continue
        if i == len(keys)+1 and n in record:
            continue
        if i>1 and i<len(keys)+1:
            if keys[i-2] + 1 == keys[i-1]:
                continue
        cases.append(i)
    for case_idx in cases:
        record_dict = {num:0 for  num in sorted(record)}
        keys = list(record_dict.keys())

        value = 1
        for i in range(len(keys)): 
            if value != case_idx:
                record_dict[keys[i]] = value
                value += 1
            else:
                record_dict[keys[i]] = value+1
                value +=2
        temp = []
        for i in range(len(record)):
            temp.append(record_dict[record[i]])
        candidate.append(tuple(temp))
    return candidate

def sort_and_select(password):
    password =  list(set(list(password)))
    password.sort()
    return password

def solution(n, m, k, records):
    answer = []
    keys = sorted(list(set(records[0])))
    if len(keys) == k:
        temp_list = [-1] +sorted(list(set(records[0].copy())))
        for i in range(len(records[0])):
            answer.append(temp_list.index(records[0][i]))
        
        return answer
    answer = get_candidate(n,m,k,records[0])
    for i in range(1, len(records)):
        new_candidate = (get_candidate(n, m, k, records[i]))

        answer = list(set(answer) & set(new_candidate))
    answer = sorted(answer, key = lambda x: sort_and_select(x))

    return list(answer[-1])


n = 8
m= 4
k=4 
records= [[1, 5, 1, 3], [5, 7, 5, 6]]
records = [[1, 5, 1, 3]]

n, m, k = 10, 3, 3
records=	[[1, 2, 3], [5, 7, 10]]
print(solution(n,m,k,records))
