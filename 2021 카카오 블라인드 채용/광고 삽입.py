from collections import defaultdict


def sec_to_time(sec):
    h, sec = sec // 3600, sec % 3600
    m, sec = sec // 60, sec % 60
    return "{0}:{1}:{2}".format(str(h).zfill(2), str(m).zfill(2), str(sec).zfill(2))


def time_to_sec(time):
    h, m, s = map(int, (time.split(":")))
    h, m = h * 60 * 60, m * 60
    return (h + m + s)


def solution(play_time, adv_time, logs):
    answer = ''
    if play_time == adv_time:
        return "00:00:00"

    play = time_to_sec(play_time)
    adv = time_to_sec(adv_time)

    dp = [0] * (play + 1)
    logs = [[time_to_sec(log.split("-")[0]),
             time_to_sec(log.split("-")[1])] for log in logs]
    for log in logs:
        start, end = log[0], log[1]
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, play):
        dp[i] = dp[i] + dp[i-1]

    for i in range(1, play):
        dp[i] = dp[i] + dp[i-1]

    mx_view, view_time = dp[adv-1], 0
    for t in range(adv, play):
        if dp[t] - dp[t - adv] > mx_view:
            mx_view = dp[t] - dp[t - adv]
            view_time = t - adv + 1

    return sec_to_time(view_time)
