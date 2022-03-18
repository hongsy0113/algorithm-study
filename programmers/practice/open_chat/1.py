## TODO: 해당 command에 대한 업데이트를 딕셔너리에 적용하는 함수
def update_dict (command, user_id, chat_room_dict, nickname=''):
    if command =='Enter' or command == 'Change':
        chat_room_dict[user_id] = nickname

# TODO : 채팅방 멤버에 대한 딕셔너리 만드는 함수
def make_dict (record, chat_room_dict):
    for string in record:
        # TODO: 해당 커맨드에 대한 처리
        if len(string) == 2:
            command, user_id = string
            update_dict(command, user_id, chat_room_dict)
        else:
            command, user_id, nickname = string
            update_dict(command, user_id, chat_room_dict, nickname)
    
#TODO: record 와 dict를 보고 result 를 출력하는 함수
def make_result(record, chat_room_dict):
    answer = []
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            msg = f'{chat_room_dict[record[i][1]]}님이 들어왔습니다.'
            answer.append(msg)
        elif record[i][0] == 'Leave':
            msg = f'{chat_room_dict[record[i][1]]}님이 나갔습니다.'
            answer.append(msg)

    return answer

def solution(record):
    #answer = []
    chat_room_dict = dict()
    for i in range(len(record)):
        record[i] = record[i].split()

    make_dict(record, chat_room_dict)
    
    answer = make_result(record, chat_room_dict)
    return answer


record = [
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]
print(solution(record))