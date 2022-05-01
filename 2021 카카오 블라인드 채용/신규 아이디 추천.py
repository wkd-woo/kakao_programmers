def solution(new_id):
    answer = new_id.lower()  # 1단계

    txt = '~!@#$%^&*()=+[{]}:?,<>/'
    if len(answer) > 0:
        for each in answer:  # 2단계
            if each in txt:
                answer = answer.replace(each, '')

    while '..' in answer:
        answer = answer.replace('..', '.')  # 3단계

    # 4단계
    while True:
        if not len(answer):  # 5단계
            answer = 'a'
        else:
            if answer[0] == '.':  # 4단계
                answer = answer[1:]
                continue
            if answer[-1] == '.':
                answer = answer[:-1]
                continue
            if len(answer) > 15:  # 6단계
                answer = answer[:15]
                continue
            if len(answer) < 3:  # 7단계
                answer += answer[-1]
                continue
            break
    return answer
