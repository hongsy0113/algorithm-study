def zip_s (answer, arr, s, x, y):
    zippable = True
    if s == 1:
        answer[arr[x][y]] += 1
        return 
    value = arr[x][y]
    for i in range(x, x+s):
        for j in range(y, y+ s):
            if arr[i][j] != value:
                zippable = False
                break
        if not zippable: break
    if zippable:
        answer[value] += 1
        return answer[value]
    else:
        s = s //2 
        points = [(x, y), (x+s, y), (x, y+s), (x+s, y+s)]
        for point in points:
            zip_s (answer, arr, s, point[0], point[1])

def solution(arr):
    answer = [0, 0]
    zip_s(answer, arr, len(arr), 0,0 )
    print(answer)
    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [
    [1,1,0,0],
    [1,1,0,0],
    [1,0,1,1],
    [0,1,1,1]
]
arr = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]
    ]

solution(arr)