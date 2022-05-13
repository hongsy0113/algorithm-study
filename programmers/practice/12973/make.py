import random

s = ''
for _ in range(1000000):
    n = random.randint(1, 1)
    # n = 1
    s += chr(n + 96)

print(s)