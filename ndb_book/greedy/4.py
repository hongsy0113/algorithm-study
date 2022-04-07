n = int(input())

coin_list = list(map(int, input().split()))

coin_list.sort()

arr = [0]

for i in coin_list:
    
    new_arr = []
    for value in arr:
        new_arr.append(value + i)
    arr = list(set(new_arr + arr))

i = 1 
while True:
    if i in arr:
        i+=1
        continue
    else:
        print(i)
        break
