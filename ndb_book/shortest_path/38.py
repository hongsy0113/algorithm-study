from collections import deque

def bfs(graph, start, visited):
    cnt = 0
    visited[start] = True
    queue = deque([start])
    while queue:
        student = queue.popleft()
        for i in graph[student]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt

def solution(graph_up, graph_down, n):
    ## 각 학생에 대해서 탐색을 하면서 점수 높은 사람 개수, 낮은 사람 개수를 구한다
    # 높은 사람 수 + 낮은 사람 수가 n-1이라면 순위를 정확히 알 수 있는 것
    cnt = 0

    for k in range(1, n+1):
        visited = [False] * (n + 1)
        ### 높은 사람을 탐색 (graph_up)
        higher_cnt = bfs(graph_up, k, visited)
        ### 낮은 사람을 탐색 (graph_down)
        lower_cnt = bfs(graph_down, k, visited)

        if higher_cnt + lower_cnt == n - 1:
            cnt += 1

    return cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph_up = [[] for _ in range(N+1)]
    graph_down = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph_up[a].append(b)
        graph_down[b].append(a)
    print(solution(graph_up, graph_down, N))
