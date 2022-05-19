def solution(n, costs):
    answer = 0

    linked_set = set([])

    # costs를 비용 적은 순으로 정렬한다
    costs.sort(key = lambda x : x[2])

    # 제일 비용 적은 간선 고르고 초기설정
    linked_set.add(costs[0][0])
    linked_set.add(costs[0][1])
    answer += costs[0][2]

    set_cnt = 1
    # 각 원소는 i번 노드가 몇번 set에 속해있는지 나타냄. -1은 안 속해 잇는 거
    idx_to_set = [-1] * n
    idx_to_set[costs[0][0]] = 1
    idx_to_set[costs[0][1]] = 1
    idx = 1
    linked_cnt = 2
    while True:
        if linked_cnt >= n and set_cnt <= 1:
            break
        edge = costs[idx]
        a, b = edge[0], edge[1]
        # 두 노드가 같은 set에 들어있는지 확인
        if idx_to_set[a] == idx_to_set[b] and idx_to_set[a] >= 0 and idx_to_set[b] >= 0:
            pass
        # 두 노드가 다른 set 에 있을 때
        elif idx_to_set[a] != idx_to_set[b] and idx_to_set[a] >= 0 and idx_to_set[b] >= 0:
            small = idx_to_set[a] if idx_to_set[a] < idx_to_set[b] else idx_to_set[b]
            big = idx_to_set[b] if idx_to_set[a] < idx_to_set[b] else idx_to_set[a]
            # 간선 추가한다
            answer += edge[2]
            # 두 set 합친다
            set_cnt -= 1
            for i in range(n):
                if idx_to_set[i] == big:
                    idx_to_set[i] = small
        # 두 노드 중 하나만 연결된 노드 일때
        elif idx_to_set[a] >= 0 and idx_to_set[b] == -1:
            # 간선 추가
            answer += edge[2]
            idx_to_set[b] = idx_to_set[a]
            # linked_cnt 증가
            linked_cnt += 1
        elif idx_to_set[b] >= 0 and idx_to_set[a] == -1:
            # 간선 추가
            answer += edge[2]
            idx_to_set[a] = idx_to_set[b]
            # linked_cnt 증가
            linked_cnt += 1
        # 두 노드 다 아직 연결 안 된 노드 일때
        else:
            # 간선 추가
            answer += edge[2]
            # set 추가
            set_cnt += 1
            nex_set_num = max(idx_to_set) + 1
            idx_to_set[a] = nex_set_num
            idx_to_set[b] = nex_set_num
            # linked_cnt 증가
            linked_cnt += 2

        idx += 1
    print(answer)
    return answer



if __name__ == '__main__':
    n = 10
    costs = 	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

    costs = [
        [0,1, 1],
        [2, 3, 1],
        [4, 5, 1],
        [6, 7, 1],
        [8, 9, 1],
        [1, 7, 7],
        [1, 4, 4],
        [2, 8, 13],
        [3, 9, 11],
        [4, 9, 10],
        [7, 8, 15],
    ]
    solution(n, costs)