def solution(files):
    answer = []
    for file in files:
        head, number, tail = [], [], []
        for i, w in enumerate(file):
            if w.isdigit():
                if not number:
                    head = file[:i]
                number.append(w)
            elif (number and not w.isdigit()) or len(number) == 5:
                tail = file[i:]
                break
        number, tail = ''.join(number), ''.join(tail)
        answer.append([head, number, tail])

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    answer = [''.join(each) for each in answer]
    return answer
