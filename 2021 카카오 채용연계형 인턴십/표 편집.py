def solution(n, k, cmd):
    nodes = {0: [n-1, 1]}
    for i in range(1, n):
        if i == n-1:
            nodes[i] = [i-1, 0]
        else:
            nodes[i] = [i-1, i+1]

    stack = []
    for c in cmd:
        if c == 'C':
            nodes[nodes[k][0]][1] = nodes[k][1]
            nodes[nodes[k][1]][0] = nodes[k][0]
            stack.append([k, nodes[k]])
            temp = nodes[k]
            del nodes[k]

            if temp[1] == 0:
                k = temp[0]
            else:
                k = temp[1]

        elif c == 'Z':  # 복구할 때 인덱스 처리 -> 삭제 전 위치로 돌아감
            curr_node, val = stack.pop()
            prev_node, next_node = val
            nodes[curr_node] = [prev_node, next_node]
            nodes[prev_node][1] = curr_node
            nodes[next_node][0] = curr_node

        else:
            c, x = c.split()
            cnt = 0
            while cnt < int(x):
                if c == 'D':
                    k = nodes[k][1]
                else:
                    k = nodes[k][0]
                cnt += 1

    answer = ['O' if nodes.get(i) else 'X' for i in range(n)]
    return ''.join(answer)
