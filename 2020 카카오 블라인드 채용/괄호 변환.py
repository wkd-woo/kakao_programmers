match = {")": "("}


def correct(s):
    stack = []
    for char in s:
        if char in match:
            top_element = stack.pop() if stack else '#'
            if match[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


def solution(p):
    if not len(p):  # 1
        return p

    if correct(p):
        return p

    u = ''
    for i in p:  # 2
        u += i
        if u.count('(') == u.count(')'):
            v = p[len(u):]
            break

    if correct(u):  # 3
        return u + solution(v)  # 3-1

    else:  # 4
        u = u[1:-1]  # 4-4
        u2 = ''  # 4-2
        for i in u:
            if i == '(':
                u2 += ')'
            else:
                u2 += '('

        return '(' + solution(v) + ')' + u2  # 4-1,4-3,4-5
