from collections import deque, defaultdict
from copy import deepcopy


def solution(n, k, cmd):
    stack = []
    table = defaultdict(list)
    now = 1
    table[0] = [i for i in range(n)]
    for i, c in enumerate(cmd):
        table[i+1] = deepcopy(table[i])
        if c == 'C':
            item = table[i+1].pop(k)
            stack.append((item, k))  # 복구를 위해 삭제될 때 위치를 저장해야함
            if k >= len(table[i+1]):
                k = len(table[i+1]) - 1

        elif c == 'Z':  # 복구할 때 인덱스 처리 -> 삭제 전 위치로 돌아감
            item, pos = stack.pop()
            table[i+1].insert(pos, item)
            if pos <= k:
                k = k + 1

        else:
            c, idx = c.split()
            idx = int(idx)
            if c == 'U':
                k = k - idx
            elif c == 'D':
                k = k + idx

    result = table[len(cmd)]
    answer = ['O' if i in result else 'X' for i in range(n)]
    return ''.join(answer)
