def dfs (nodes, pos):
    # 방문처리
    nodes[pos[0]][pos[1]] = 1
    # 가능한 인접 노드의 좌표(x, y)
    adj_nodes_pos = []

    if pos[0]+1 < len(nodes):
        adj_nodes_pos.append((pos[0]+1, pos[1]))
    if pos[1]+1 < len(nodes[0]):
        adj_nodes_pos.append((pos[0], pos[1]+1))
    if pos[0] > 0:
        adj_nodes_pos.append((pos[0]-1, pos[1]))
    if pos[1] > 0:
        adj_nodes_pos.append((pos[0], pos[1]-1))
    
    for adj_pos in adj_nodes_pos:
        # 인접하는 노드가 얼음이라면 재귀함수 호출
        if nodes[adj_pos[0]][adj_pos[1]] == 0:
            dfs(nodes, adj_pos)

n, m = map(int, input().split())

nodes = [list(map(int, str(input()))) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if nodes[i][j] == 0:
            dfs(nodes, (i, j))    
            count += 1

print(count)