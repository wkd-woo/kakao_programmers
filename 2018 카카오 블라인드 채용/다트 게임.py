def solution(dartResult):
    score = []
    num = ''
    for each in dartResult:
        if each.isdigit():
            num += each
        else:
            if len(num):
                score.append(int(num))
                num = ''
            if each == '*':
                score[-1] = score[-1] * 2
                if len(score) > 1:
                    score[-2] = score[-2] * 2
            elif each == '#':
                score[-1] = score[-1] * (-1)
            elif each == 'D':
                score[-1] = score[-1] ** 2
            elif each == 'T':
                score[-1] = score[-1] ** 3

    answer = sum(score)
    return answer
