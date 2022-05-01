def solution(id_list, report, k):
    success = dict()
    from_to = dict()
    cnt_report = dict()
    for each in id_list:
        from_to[each] = set()
        cnt_report[each] = 0
        success[each] = 0

    for each in report:
        reporter, reported = each.split()
        if reported in from_to[reporter]:
            pass
        else:
            from_to[reporter].add(reported)
            cnt_report[reported] += 1

    ban = [key for key, value in cnt_report.items() if value >= k]
    for i in ban:
        for each in from_to:
            if i in from_to[each]:
                success[each] += 1
    answer = list(success.values())

    return answer