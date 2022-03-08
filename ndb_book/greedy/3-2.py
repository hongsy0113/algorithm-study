n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

cur_m, cur_k = 0, 0
result = 0


while (m>0):
    if cur_k < k:
        result += num_list[0]
        cur_k += 1
        m -= 1
    else:
        result += num_list[1]
        cur_k =0
        m -= 1

print(result)