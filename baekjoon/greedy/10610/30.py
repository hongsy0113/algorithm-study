n = int(input())

digit_list = list(map(int, str(n)))

s = sum(digit_list)

if (not 0 in digit_list) or s % 3 != 0:
    result = -1
else:
    digit_list.sort(reverse=True)
    digit_str_list = list(map(str, digit_list))
    result = int(''.join(digit_str_list))

print(result)