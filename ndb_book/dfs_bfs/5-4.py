from collections import deque

# bfs 정의 
def bfs(nodes, start_pos, visited):
    depth = 1
    
    # 탈출하는 최단거리를 알기 위해서는 depth를 카운트 해야하므로 queue에 depth에 대한 정보도 같이 push
    queue = deque([(start_pos, depth)])
    visited.append(start_pos)
    
    while queue:
        pos, depth = queue.popleft()
        depth += 1
        # 이동가능한 상하좌우 노드들
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
            # 목적지에 도착하면 그 즉시 depth를 반환하고 종료
            if adj_pos == (len(nodes)-1, len(nodes[0])-1):
                return depth
            if nodes[adj_pos[0]][adj_pos[1]] == 1 and not adj_pos in visited:
                queue.append((adj_pos, depth))
                visited.append(adj_pos)

    return depth

n, m = map(int, input().split())

nodes = [list(map(int, str(input()))) for _ in range(n)]

count = 0 

visited = []

print(bfs(nodes, (0,0), visited))