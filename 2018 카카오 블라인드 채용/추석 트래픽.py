def solution(lines):
    answer = 0
    logs = []

    for line in lines:
        date, s, t = line.split()
        s, t = s.split(':'), t.replace('s', '')

        end = (int(s[0]) * 3600 + int(s[1])*60 +
               float(s[2])) * 1000  # 시, 분, 초를 밀리초로 변환
        start = end - float(t) * 1000 + 1
        logs.append([start, end])

    for log in logs:  # 초당 처리량 계산,
        answer = max(answer, throughput(
            logs, log[0], log[0] + 1000), throughput(logs, log[1], log[1] + 1000))

    return answer


# 초당 처리량 계산
def throughput(logs, start, end):
    cnt = 0
    for log in logs:
        if log[0] < end and log[1] >= start:
            cnt += 1

    return cnt
