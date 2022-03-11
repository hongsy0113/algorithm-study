from secrets import choice
import sys

def search (graph, v, visited, team):
    visited[v] = True
    team.append(v)
    # 자가지신을 선택한 경우
    if graph[v] == v:
        # 첫 start가 자기자신이면 자기자신 한명을 팀으로 return
        if len(team) == 1:
            return team
        # 다른데서 start했는데 self cycle 만나면 team이 될 수 없으므로 빈 배열
        else:
            ## 나중에 자기차례에 팀으로 count 되어야 하므로 visited false로
            visited[v] = False
            return []
    # 다음 노드가 이미 team에 들어있다는 것은 cycle이 형성됐다는 것이므로 해당 team 리턴
    elif graph[v] in team:
        return team
    # 다음 노드가 방문한 적이 있다는 것은 team에 속해있든 아니든 새 팀이 만들어 질 수 없다
    elif visited[graph[v]]:
        return [] 
    # 다음 노드에 대해서 search 진행
    else:
        team = search(graph, graph[v], visited, team)
    # return 넣어줘야 함
    return team

def main():
    T = int(sys.stdin.readline())
    
    # 결과 저장할 리스트
    result = []

    for i in range(T):
        # 입력 파트
        n = int(sys.stdin.readline())
        choices = [0] + list(map(int, sys.stdin.readline().split()))
        not_in_team = [i for i in range(1, n+1)]
        visited = [False] * (n+1)
        for v in range(1, n+1):
            if visited[v] == False:
                # 해당 노드에 대해 탐색 후 팀이 만들어졌다면 학생 번호 리스트, 그렇지 않다면 빈리스트 반환
                new_team = search(choices, v, visited, [])
                if new_team:
                    # 팀 형성된 애들은 리스트에서 지워준다.
                    not_in_team = [i for i in not_in_team if i not in new_team]
        
        result.append(len(not_in_team))

    for num in result:
        print(num)

if __name__ == '__main__':
    main()