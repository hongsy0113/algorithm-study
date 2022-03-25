# 여행경로
def get_adjacent(airport, tickets):
    adjacency_dict = {}
    for ticket in tickets:
        if not ticket[0] in adjacency_dict:
            adjacency_dict[ticket[0]] = [ticket[1]]
        else:
            adjacency_dict[ticket[0]].append(ticket[1])

def get_adjacent(airport, tickets, used):
    adj_list = []
    for i in range(len(tickets)):
        if tickets[i][0] == airport and used[i] == False:
            # 인접한 공항과 해당 티켓의 인덱스를 저장
            adj_list.append((tickets[i][1], i))
    adj_list.sort()

    return adj_list

route = []

def dfs(tickets, v, used):
    print(v, end='  ')
    route.append(v)
    adj_list = get_adjacent(v, tickets, used)
    print(adj_list)
    if  (False in used) and len(adj_list)==0:
        print('fail')
        print('beforepop', route)
        route.pop()
        print('after pop', route)
        return False
    if not False in used:
        return True
    is_available = False
    for (airport,i) in adj_list:
        if used[i] == False:
            used[i] = True
            if dfs(tickets, airport, used) == False:
                used[i] = False
                
            else:
                is_available = True
    if is_available == False:
        route.pop()
        return False
    return True


def solution(tickets):
    # 여러번 방문하더라도 티켓을 전부 사용하는 게 목적이므로 티켓의 사용여부를 저장
    used = [False] * len(tickets)
    dfs(tickets, 'ICN', used)
    print('route', route)
    return route

#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ICN"]]
tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
print(solution(tickets))