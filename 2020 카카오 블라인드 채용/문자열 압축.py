def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        res = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s), i):
            if temp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    res = res + str(cnt) + temp
                else:
                    res = res + temp
                temp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            res = res + str(cnt) + temp
        else:
            res = res + temp
        result.append(len(res))

    return min(result)