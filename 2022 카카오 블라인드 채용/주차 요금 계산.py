from math import ceil


def solution(fees, records):
    lot = dict()  # 주차장
    reports = dict()  # 체류시간 쌓아 놈
    result = dict()  # 정산

    for k in records:
        num = k.split()[1]  # 차량번호
        reports[num] = 0
        result[num] = 0
        lot[num] = -1

    for i in records:
        h, m = i.split()[0].split(':')  # 몇시 몇분
        num = i.split()[1]  # 차량번호
        log = i.split()[2]  # 내역
        t = 60 * int(h) + int(m)  # 현재시각(분) = 시간 * 60 + 분
        if log == 'IN':  # 들어오면
            lot[num] = t  # 주차장에 시간기록
        elif log == 'OUT':  # 나가면
            used = t - lot[num]  # 현재시각에서 주차장 들어온시간 뺌
            reports[num] += used  # 체류시간 쌓아 놓는다
            lot[num] = -1  # 주차장은 다시 비워둔다

    for i in lot:
        if lot[i] != -1:  # 만약에 주차장에 차가 아직 있으면
            used = 1439 - lot[i]  # 2359에 내쫓는다
            reports[i] += used  # 체류시간 쌓아 놓는다

    for i in reports:
        result[i] += fees[1]
        if reports[i] > fees[0]:
            result[i] += (ceil((reports[i] - fees[0]) / fees[2])) * fees[3]

    answer = []
    for i in sorted(result.keys()):
        answer.append(result[i])
    return answer
