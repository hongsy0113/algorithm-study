n, m = map(int, input().split())

min_list = []

for i in range(n):
    row = list(map(int, input().split()))
    min_list.append(min(row))

result = max(min_list)

print(result)
