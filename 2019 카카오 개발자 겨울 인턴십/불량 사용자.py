from itertools import permutations


def check(ui, bi):
    if len(ui) != len(bi):
        return False
    for u, b in zip(ui, bi):
        if u == b or b == '*':
            pass
        else:
            return False
    return True


def solution(user_id, banned_id):
    answer = set()
    for each in permutations(user_id, len(banned_id)):
        cnt = 0
        for e, b in zip(each, banned_id):
            if check(e, b):
                cnt += 1

        if cnt == len(banned_id):
            answer.add(''.join(sorted(each)))

    return len(answer)
