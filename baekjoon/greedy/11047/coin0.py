n, k = map(int, input().split())

coin_list = []
count = 0

for i in range(n):
    value = int(input())
    if value <= k:
        coin_list.append(value)

coin_list.reverse()

## 시간초과
# i = 0
# while True:
#     coin = coin_list[i]
#     if coin <= k:
#         k -= coin
#         count += 1
#     else:
#         i += 1
#     if k <= 0 :
#         break
for i in coin_list:
    if k >= i:
        num = k // i
        k -= i * num
        count += num
    else:
        continue
print(count)