import sys 
from itertools import permutations
input = sys.stdin.readline
# 완전탐색으로 풀어보자
MAX = 1000000001
MIN = -1000000001

def operation(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if a<0 and b>0:
            a = -a
            return - (a//b)
        return a//b

N = int(input())
a_list = list(map(int, input().split()))
op_cnt_list = list(map(int, input().split()))

op_list = []
op = ['+', '-', '*', '/']
for i in range(4):
    for _ in range(op_cnt_list[i]):
        op_list.append(op[i])

it = permutations(op_list, len(op_list))

max_value = MIN
min_value = MAX
for ops in it:
    value = operation(a_list[0], a_list[1], ops[0])
    for i in range(2, N):
        value = operation(value, a_list[i], ops[i-1])
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(max_value)
print(min_value)



print(-2 // -2)
print(operation(-2, -2, '/'))
print(-5 // -3)
print(operation(-5, -3, '/'))
print(-7//3)
print(operation(-7, 3, '/'))