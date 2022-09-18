def solution(m, musicinfos):
    answer = ''
    db = {}
    m = list(m)
    for i, each in enumerate(m):
        if each == '#':
            m[i-1] = m[i-1] + '#'
    m = [each for each in m if each != '#']

    for k, musicinfo in enumerate(musicinfos):
        start, end, title, notes = musicinfo.split(',')
        end, start = list(map(int, end.split(':'))), list(
            map(int, start.split(':')))
        end[0], start[0] = end[0] * 60, start[0] * 60
        재생시간 = sum(end) - sum(start)
        notes = list(notes)
        for i, each in enumerate(notes):
            if each == '#':
                notes[i-1] = notes[i-1] + '#'
        notes = [each for each in notes if each != '#']

        if len(notes) == 재생시간:
            temp = notes
        elif len(notes) > 재생시간:
            temp = notes[:재생시간+1]
        else:
            temp = notes[:재생시간] * (재생시간//len(notes)) + \
                notes[:재생시간 % len(notes)+1]

        # 1. 들은 시간 < 재생 시간
        if len(m) <= len(temp):
            for i in range(len(temp)):
                each = (temp*3)[i:i+len(m)]
                if ''.join(m) == ''.join(each):
                    db[title] = (재생시간, k)
                    break

        # 2. 들은 시간 > 음악 시간
        else:
            for i in range(len(m)):
                each = (temp*3)[i:i+len(m)]
                if ''.join(m) == ''.join(each):
                    db[title] = (재생시간, k)
                    break

    mx, idx = -int(1e9), int(1e9)
    for K, V in db.items():
        if V[0] > mx:
            mx, idx = V
            answer = K
        elif V[0] == mx and V[1] < idx:
            mx, idx = V
            answer = K

    return answer if answer else '(None)'
