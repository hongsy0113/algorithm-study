
def solution(n, clockwise):
    # answer를 0으로 초기화해두고 0으로 칠한다
    #answer = [[]]
    answer = [[0]*n for _ in range(n)]

    if n==1: return [[1]]

    ## TODO
    # 우선 한 줄기만 시도해보자
    ## 1 부터 n 까지 인덱스에 대한 for문을 돌면서 answer에 해당하는  값 채워넣기
    ## 이미 채워져 있다면 꺽어야 됨. 값이 0이 아니라면
    points = [[0, 0], [0, n-1], [n-1, n-1],  [n-1, 0]]
    
    ## TODO : 방향을 가리키는 리스트도 만들자. 만약에 꺾어야 하는 상황이 오면 방향 벡터를 바꾸도록
    if clockwise:
        directions = [[0, 1], [1, 0],  [0, -1], [-1, 0]]
    else:
        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # TODO : 네 개의 좌표가 있을 때 해당 좌표들 입력 값으로 칠하는 함수
    # 동시에  네칸이 같은 값 적는 것도 고려. 그건 solution에서 고려해도 될 듯
    def check_point (points, value):
        for point in points:
            answer[point[0]][point[1]]  = value

    ## TODO: 현재 좌표들에 direction 적용하는 함수
    def move(points, direction):
        for i in range(len(points)):
            points[i][0] += direction[i][0]
            points[i][1] += direction[i][1]

    ## TODO: 방향 꺾는 함수. clockwise 인자로 받는다
    def change_direction(directions, clockwise):
        if clockwise:
            # 시계방향이면 리스트 왼쪽 이동
            directions.append(directions[0])
            directions.remove(directions[0])
            return directions
        else:
            # 오른쪽 이동
            
            left = [directions[3]]
            right = directions[0:3]
            directions = left + right
            return directions

    check_point (points, 1)
    #for i in range(2, 100):
    i=2
    while True:
        # TODO move가 가능한지 확인
        if answer[points[0][0] + directions[0][0]][points[0][1]+ directions[0][1]] == 0:
            ## 가능하다면 move
            move(points, directions)
            ## move 후 i 값으로 check
            check_point(points, i)
            i +=1
            continue
        else:
            ## 불가능 하다면 direction을 바꾼다
            directions = change_direction(directions, clockwise)
            ## 방향 바꿔도 칠해져 있으면 종료
            if answer[points[0][0] + directions[0][0]][points[0][1]+ directions[0][1]] != 0:
                break
            

    return answer

# n = 5
# clockwise = False
n = 50
clockwise = True
result = (solution(n, clockwise))
for row in result:
    print(row)