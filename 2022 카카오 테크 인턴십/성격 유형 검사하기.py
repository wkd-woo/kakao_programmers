def solution(survey, choices):
    answer = ''
    one = dict()
    two = dict()
    three = dict()
    four = dict()

    one['R'] = 0
    one['T'] = 0
    two['C'] = 0
    two['F'] = 0
    three['J'] = 0
    three['M'] = 0
    four['A'] = 0
    four['N'] = 0

    for i in range(len(survey)):
        opt = list(survey[i])
        if 'R' in opt:  # 1
            if choices[i] == 1:
                one[opt[0]] += 3
            elif choices[i] == 2:
                one[opt[0]] += 2
            elif choices[i] == 3:
                one[opt[0]] += 1
            elif choices[i] == 4:
                pass
            elif choices[i] == 5:
                one[opt[1]] += 1
            elif choices[i] == 6:
                one[opt[1]] += 2
            elif choices[i] == 7:
                one[opt[1]] += 3
        if 'C' in opt:  # 1
            if choices[i] == 1:
                two[opt[0]] += 3
            elif choices[i] == 2:
                two[opt[0]] += 2
            elif choices[i] == 3:
                two[opt[0]] += 1
            elif choices[i] == 4:
                pass
            elif choices[i] == 5:
                two[opt[1]] += 1
            elif choices[i] == 6:
                two[opt[1]] += 2
            elif choices[i] == 7:
                two[opt[1]] += 3
        if 'J' in opt:  # 1
            if choices[i] == 1:
                three[opt[0]] += 3
            elif choices[i] == 2:
                three[opt[0]] += 2
            elif choices[i] == 3:
                three[opt[0]] += 1
            elif choices[i] == 4:
                pass
            elif choices[i] == 5:
                three[opt[1]] += 1
            elif choices[i] == 6:
                three[opt[1]] += 2
            elif choices[i] == 7:
                three[opt[1]] += 3
        if 'A' in opt:  # 1
            if choices[i] == 1:
                four[opt[0]] += 3
            elif choices[i] == 2:
                four[opt[0]] += 2
            elif choices[i] == 3:
                four[opt[0]] += 1
            elif choices[i] == 4:
                pass
            elif choices[i] == 5:
                four[opt[1]] += 1
            elif choices[i] == 6:
                four[opt[1]] += 2
            elif choices[i] == 7:
                four[opt[1]] += 3

    if one['R'] == one['T']:
        answer += 'R'
    else:
        if one['R'] > one['T']:
            answer += 'R'
        else:
            answer += 'T'

    if two['C'] == two['F']:
        answer += 'C'
    else:
        if two['C'] > two['F']:
            answer += 'C'
        else:
            answer += 'F'

    if three['J'] == three['M']:
        answer += 'J'
    else:
        if three['J'] > three['M']:
            answer += 'J'
        else:
            answer += 'M'

    if four['A'] == four['N']:
        answer += 'A'
    else:
        if four['A'] > four['N']:
            answer += 'A'
        else:
            answer += 'N'

    return answer
