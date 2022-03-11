import sys

N = int(input())

work_list = []

for i in range(N):
    work_list.append(tuple(map(int, sys.stdin.readline().split())))

# 일찍 끝나는 시간 순으로 정렬
work_list.sort(key= lambda x: (x[1], x[0]))

cur_finish = 0
count = 0
print("work_list" ,work_list)
for work in work_list:
    # 제일 일찍 끝나는 회의 선택( 리스트에서 제거 )
    if work[0] >= cur_finish:
        count += 1
        cur_finish = work[1]
print(count)