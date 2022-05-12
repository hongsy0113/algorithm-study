import heapq
INF = int(1e9)


def dijkstra(graph, distance):
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    distance = [INF] * (N + 1)
    dijkstra(graph, distance)
    # distance를 순회하면서 정렬용 튜플의 리스트 만들기
    result_dict = {}
    max_dist = -1
    for i in range(1, N+1):
        if distance[i] > max_dist:
            max_dist = distance[i]
        if distance[i] in result_dict:
            result_dict[distance[i]].append(i)
        else:
            result_dict[distance[i]] = [i]

    first = sorted(result_dict[max_dist])[0]
    second = max_dist
    third = len(result_dict[max_dist])

    print(first, second, third)