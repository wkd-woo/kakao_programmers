def solution(s):
    answer = []

    s = s[2:-2].split('},{')

    s.sort(key=lambda x: len(x))
    s = [list(map(int, i.split(','))) for i in s]
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                
    return answer