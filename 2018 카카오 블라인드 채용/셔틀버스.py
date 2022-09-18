from collections import deque


def convert_min(s):
    h, m = s.split(':')
    return int(h) * 60 + int(m)


def convert_time(m):
    h, m = str(m // 60), str(m % 60)
    return h.zfill(2) + ":" + m.zfill(2)


def solution(n, t, m, timetable):
    timetable = deque(
        sorted(each for each in timetable if each != "23:59"))  # 23:59에는 집에 감
    timetable = deque(map(convert_min, timetable))
    start = convert_min("09:00")
    max_of_passengers = n * m

    if not timetable:  # 무조건 탈 수 있는 경우
        return convert_time(start + t * (n-1))

    while n > 1:  # 마지막 버스 전까지 남아있는 동안
        for _ in range(m):
            if timetable and start >= timetable[0]:
                timetable.popleft()
        n -= 1
        start += t

    if len(timetable) + 1 <= m:
        return convert_time(start)

    if len(timetable) + 1 > m:
        return convert_time(timetable[m-1] - 1)
