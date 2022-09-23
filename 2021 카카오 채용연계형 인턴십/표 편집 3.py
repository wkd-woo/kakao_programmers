from collections import deque


def solution(n, k, cmd):
    stack = []
    l = [i for i in range(n)]
    db = set(i for i in range(n))
    l_q, r_q = deque(l[:k]), deque(l[k:])

    for c in cmd:
        if not r_q:
            r_q.append(l_q.pop())

        if r_q and c == 'C':
            item = r_q.popleft()
            stack.append((item, len(l_q)))  # 복구를 위해 삭제될 때 위치를 저장해야함
            db.remove(item)

        elif c == 'Z':  # 복구할 때 인덱스 처리 -> 삭제 전 위치로 돌아감
            now = r_q[0]
            item, pos = stack.pop()
            temp = list(l_q + r_q)
            temp.insert(pos, item)
            now = temp.index(now)
            l_q, r_q = deque(temp[:now]), deque(temp[now:])
            db.add(item)
        else:
            c, idx = c.split()
            idx = int(idx)
            if c == 'U':
                for _ in range(idx):
                    if l_q:
                        r_q.appendleft(l_q.pop())
                    else:
                        break
            elif c == 'D':
                for _ in range(idx):
                    if r_q:
                        l_q.append(r_q.popleft())
                    else:
                        break

    answer = ['O' if i in db else 'X' for i in range(n)]
    return ''.join(answer)
