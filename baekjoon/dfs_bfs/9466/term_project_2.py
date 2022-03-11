from secrets import choice
import sys

# def search (graph, v, visited, team):
#     if graph[v] == v:



#     # 자가지신을 선택한 경우
#     if graph[v] == v:
#         # 첫 start가 자기자신이면 자기자신 한명을 팀으로 return
#         if len(team) == 1:
#             return team
#         # 다른데서 start했는데 self cycle 만나면 team이 될 수 없으므로 빈 배열
#         else:
#             ## 나중에 자기차례에 팀으로 count 되어야 하므로 visited false로
#             visited[v] = False
#             return []
#     # 다음 노드가 이미 team에 들어있다는 것은 cycle이 형성됐다는 것이므로 해당 team 리턴
#     elif graph[v] in team:
#         return team
#     # 다음 노드가 방문한 적이 있다는 것은 team에 속해있든 아니든 새 팀이 만들어 질 수 없다
#     elif visited[graph[v]]:
#         return [] 
#     # 다음 노드에 대해서 search 진행
#     else:
#         team = search(graph, graph[v], visited, team)
#     # return 넣어줘야 함
#     print("team: ", team)
    
#     return team

def search(graph):
    in_team_count = 0
    # 아무 노드 선택
    if list(graph.keys()):
            node = list(graph.keys())[0]
    while True:
        
        # 다음 노드가 그래프에 없을 때 (삭제 되었을 때)
        if graph[node] not in graph:
            del graph[node]
            continue
        # 다음 노드가 존재할 때
        elif graph[node] == node:
            # cycle
            in_team_count += 1
            del graph[node]
            continue
        elif 


def main():
    T = int(sys.stdin.readline())
    
    # 결과 저장할 리스트
    result = []

    for _ in range(T):
        # 입력 파트
        n = int(sys.stdin.readline())

        ## dict로 받아보자
        
        key = [i for i in range(1, n+1)]
        choices = dict(zip(key, list(map(int, sys.stdin.readline().split()))))
        
        # not_in_team = [i for i in range(1, n+1)]
        visited = [False] * (n+1)
        
        search(choices)

    
if __name__ == '__main__':
    main()



### dict 로 하다가 포기