def solution(n, clockwise):
    
    answer = [[0]*n for _ in range(n)]

    if n==1: return [[1]]

    points = [[0, 0], [0, n-1], [n-1, n-1],  [n-1, 0]]
    
    if clockwise:
        directions = [[0, 1], [1, 0],  [0, -1], [-1, 0]]
    else:
        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        
    def check_point (points, value):
        for point in points:
            answer[point[0]][point[1]]  = value

    def move(points, direction):
        for i in range(len(points)):
            points[i][0] += direction[i][0]
            points[i][1] += direction[i][1]

    def change_direction(directions, clockwise):
        if clockwise:
            directions.append(directions[0])
            directions.remove(directions[0])
            return directions
        else:            
            left = [directions[3]]
            right = directions[0:3]
            directions = left + right
            return directions

    check_point (points, 1)
    i=2
    while True:
        if answer[points[0][0] + directions[0][0]][points[0][1]+ directions[0][1]] == 0:
            move(points, directions)
            check_point(points, i)
            i +=1
            continue
        else:
            directions = change_direction(directions, clockwise)
            if answer[points[0][0] + directions[0][0]][points[0][1]+ directions[0][1]] != 0:
                break
            

    return answer