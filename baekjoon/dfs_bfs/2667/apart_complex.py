import sys

# TODO 해당 노드의 이웃 알려주는 함수
# n by n 넘어가는지, 0인지 1인지만 고려
def get_neighbor(graph, v, n):
    neighbors =[]
    pos = (v[0]-1, v[1]) # 상
    if pos[0] >= 0 and graph[pos[0]][pos[1]] != 0:
        neighbors.append(pos)
    pos = (v[0]+1, v[1]) # 하
    if pos[0] < n and graph[pos[0]][pos[1]] != 0:
        neighbors.append(pos)
    pos = (v[0], v[1]-1) # 좌
    if pos[1] >= 0 and graph[pos[0]][pos[1]] != 0:
        neighbors.append(pos)
    pos = (v[0], v[1]+1) # 우
    if pos[1] < n and graph[pos[0]][pos[1]]!= 0:
        neighbors.append(pos)
    return neighbors

def dfs(graph, v,  complex_num, count):
    # 단지 내 집 수 증가
    count += 1
    # 해당 위치에 해당하는 단지번호 매겨준다.
    graph[v[0]][v[1]] = complex_num
    neighbors = get_neighbor(graph, v, len(graph))

    for neighbor in neighbors:
        if graph[neighbor[0]][neighbor[1]] == 1:
            count = dfs(graph, neighbor, complex_num, count)

    return count

def solve():
    n = int(sys.stdin.readline())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().strip())))

    complex_num = 2
    house_count = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
            ## TODO: 모든 방문하지 않은 집에 대해서 탐색 진행
                house_count.append(dfs(arr, (i, j), complex_num,0 ))
                complex_num += 1
    # 단지수 출력
    print(complex_num-2)
    # 단지내 집의 수 오름차순으로 정렬하고 출력
    house_count.sort()
    for count in house_count:
        print(count)

if __name__ == '__main__':
    solve()
