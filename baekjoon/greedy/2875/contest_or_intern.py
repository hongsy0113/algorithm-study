n, m, k = map(int, input().split())

for i in range(k):
    female_max = n//2
    male_max = m
    diff = female_max - male_max
    if diff > -1:
        n -= 1
    else:
        m -= 1
    
max_team = min(n//2, m)

print(max_team)