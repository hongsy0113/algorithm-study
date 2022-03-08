n, m = map(int, input().split())

if n == 1:
    result = 1
elif n == 2:
    result = min(4, (m+1)//2)
elif m <=6:
    result = min(4, m)
else:
    result = m-2

print(result)

'''
pos = [1, 1]
constraints = [0, 1, 2, 3]

result = 1
if n == 1 or m == 1:
    result = 1
elif m <= 4 and n >= 3:
    result = m
elif m <=4 and n == 2:
    result = 2 if  m>= 3 else 1
else:
    while True:
        if constraints:
            if n - pos[1] >= 2 and m - pos[0] >= 1 and 0 in constraints:
                pos[0] += 1
                pos[1] += 2
                result += 1
                constraints.remove(0)
                print('0')
                print_pos(pos)
                continue
            elif pos[1] >= 2 and m - pos[0] >= 1  and 1 in constraints:
                pos[0] += 1
                pos[1] -= 2
                result += 1
                constraints.remove(1)
                print('1')
                print_pos(pos)
                
                continue
            elif n - pos[1] >= 1 and m - pos[0] >=2 and 2 in constraints:
                pos[0] += 2
                pos[1] += 1
                result += 1
                constraints.remove(2)
                print('2')
                print_pos(pos)
                continue
            elif pos[1] >= 1 and m - pos[0] >=2 and 3 in constraints:
                pos[0] += 2
                pos[1] -= 1
                result += 1
                constraints.remove(3)
                print('3')
                print_pos(pos)
                continue
        else:
            if n - pos[1] >= 2 and m - pos[0] >= 1:
                pos[0] += 1
                pos[1] += 2
                result += 1
                print_pos(pos)
                continue
            elif pos[1] >= 2 and m - pos[0] >= 1:
                pos[0] += 1
                pos[1] -= 2
                result += 1
                print_pos(pos)
                continue
        break
print(result)
'''