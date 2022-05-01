def solution(record):
    nick_db = dict()
    result = []
    for i in record:
        c = i.split()[0]
        uid = i.split()[1]
        if len(i.split()) > 2:
            nickname = i.split()[2]
        if c == 'Enter':
            nick_db[uid] = nickname
            result.append(('Enter', uid))
        elif c == 'Leave':
            result.append(('Leave', uid))
        else:
            nick_db[uid] = nickname
    answer = []
    for j in result:
        if j[0] == 'Enter':
            answer.append(f"{nick_db[j[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nick_db[j[1]]}님이 나갔습니다.")
    return answer
