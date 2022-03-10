pos = input()

colunm_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

row = int(pos[1])
col = colunm_dict[pos[0]]

if row >=3 and row <=6 :
    if col >=3 and col <=6:
        result = 8
    elif col ==2 or col ==7:
        result = 6
    else:
        result = 4
elif row == 2 or row ==7:
    if col >=3 and col <=6:
        result = 6
    elif col == 2 or col == 7:
        result = 4
    else:
        result = 3
else:
    if col >=3 and col <=6:
        result = 4
    else:
        result = 2
print(result)

# #######
# 교재 답안 코드

# row = int(pos[1])
# column = int(ord(pos[0])) - int (ord('a')) + 1

# steps = [
#     (-2, -1), (-1, -2), (1, -2), (2,-1),
#     (2, 1), (1,2), (-1, 2), (-2,1)
# ]

# r = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8 :
#         r += 1

# print(r)

# 교재 답안 코드와 내 코드 같은지 확인
# while True:
#     pos = input()

#     colunm_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

#     row = int(pos[1])
#     col = colunm_dict[pos[0]]

#     if row >=3 and row <=6 :
#         if col >=3 and col <=6:
#             result = 8
#         elif col ==2 or col ==7:
#             result = 6
#         else:
#             result = 4
#     elif row == 2 or row ==7:
#         if col >=3 and col <=6:
#             result = 6
#         elif col == 2 or col == 7:
#             result = 4
#         else:
#             result = 3
#     else:
#         if col >=3 and col <=6:
#             result = 4
#         elif col == 2 or col == 7:
#             result = 3
#         else:
#             result = 2
#     print(result)

#     #######33
#     row = int(pos[1])
#     column = int(ord(pos[0])) - int (ord('a')) + 1

#     steps = [
#         (-2, -1), (-1, -2), (1, -2), (2,-1),
#         (2, 1), (1,2), (-1, 2), (-2,1)
#     ]

#     r = 0
#     for step in steps:
#         next_row = row + step[0]
#         next_column = column + step[1]
#         if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8 :
#             r += 1

#     print(r)
#     if r == result:
#         print("same!!")
#     else:
#         print("wrong!!!!!!!!!!!")