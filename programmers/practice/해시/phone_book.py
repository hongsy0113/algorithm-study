def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(min(phone_book))

    my_dict = {}
    for number in phone_book:
        for i in range(n, len(number)):
            key = number[:i]
            print('key', key)
            if key in my_dict:
                return False
        my_dict[number] = 1
        print(my_dict)
    return answer

### 참고 답안
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        # if p2.startswith(p1):
        #     return False
    return True

phone_book = ["12","123","1235","567","88"]
print(solution2(phone_book))

arr = ['128', '12', '121', '33', '1', '11', '21', '9']
arr.sort()
print((arr))