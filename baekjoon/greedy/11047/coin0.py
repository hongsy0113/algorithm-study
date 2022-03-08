n, k = map(int, input().split())

coin_list = []
count = 0

for i in range(n):
    coin_list.append(int(input()))

coin_list.reverse()

i = 0
while True:
    coin = coin_list[i]
    if coin <= k:
        k -= coin
        count += 1
    else:
        i += 1
    if k <= 0 :
        break

print(count)