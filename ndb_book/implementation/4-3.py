n, m = map(int, input().split())

a, b, d = map(int, input().split())

game_map = [list(map(int,input().split())) for _ in range(n)]

visited = [(a,b)]

count = 1

d_step_dict = {0:[-1, 0], 1: [0, 1], 2:[1, 0], 3:[0, -1]}
new_pos = ()

while True:
    moved = False

    for i in range(d+3,d-1, -1):
        i %= 4

        new_pos = (a + d_step_dict[i][0], b + d_step_dict[i][1])

        if game_map[new_pos[0]][new_pos[1]] == 0 and (not new_pos in visited):
            a = new_pos[0]
            b = new_pos[1]
            d = i
            visited.append(new_pos)
            print(new_pos)
            print(d)
            moved = True
            count += 1
            break

    if moved == False:
        back_step = d_step_dict[(d-2)%4]
        new_pos = (a + back_step[0], b + back_step[1])
        print("back", new_pos)
        if game_map[new_pos[0]][new_pos[1]] == 1:
            break
        (a,b) = new_pos
print(count)
