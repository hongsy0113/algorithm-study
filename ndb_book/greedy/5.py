
n, m = map(int, input().split())

weights = list(map(int, input().split()))
weights.sort()

cnt = 0
for i in range(n-1):
    if weights[i] != weights[i+1]:
        cnt += n - i - 1
    else:
        for j in range(i+1, n+1):
            if j == n: break
            if weights[j] != weights[i]:
                break
        cnt += n-j
print(cnt)