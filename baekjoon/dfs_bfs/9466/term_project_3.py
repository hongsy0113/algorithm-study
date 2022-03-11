import sys

def make_team (choices, n):
    is_in_team = [0] * (n + 1)
    # 각 학생에 대한 팀 배정 여부를 list로 담는다
    # 0: 아직 미배정 1: 팀 결정 -1: 팀 없음
    for i in range(1, n+1):
        # 이미 결정났다면 진행할 필요 x
        if is_in_team[i] != 0: continue
        temp_team = [i]

        for j in range(0, n+1):
            # 다음 노드가 선택 될 수 없다면
            if is_in_team[choices[temp_team[j]]] != 0:
                # print('case 1')
                # temp_team 리스트 j번째 학생까지는 팀을 만들 수 없다
                
                for student in temp_team:
                    is_in_team[student] = -1
                break
            else:
                # 자기자신을 선택한 경우
                if temp_team[j] == choices[temp_team[j]]:
                    # print('case 2')
                    is_in_team[temp_team[j]] = 1
                    temp_team.remove(temp_team[j])
                    # 다른 temp_team에 있던 학생들은 팀을 만들 수 없다.
                    
                    for student in temp_team:
                        is_in_team[student] = -1
                    break
                # 이미 temp team에 있는 경우 -> cycle
                elif choices[temp_team[j]] in temp_team:
                    # print('case 3')
                    for student in temp_team:
                        is_in_team[student] = 1
                    break
                else:
                    # 선택한 학생도 temp team에 넣는다
                    # print('case 4')
                    temp_team.append(choices[temp_team[j]])
    print(is_in_team)
    # print(len([i for i in is_in_team if i==-1]))
    return len([i for i in is_in_team if i==-1])

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

        result.append(make_team(choices, n))
    for num in result:
        print(num)
    
if __name__ == '__main__':
    main()



### dict 로 하다가 포기