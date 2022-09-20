def solution(info, edges):
    global answer
    answer = 0
    graph = {i: [] for i in range(len(info))}

    def dfs(cur, sheep, wolf, path=[]):
        sheep += (info[cur] == 0)
        wolf += info[cur]
        global answer
        answer = max(answer, sheep)

        if wolf >= sheep:
            return

        path.extend(graph[cur])
        for p in path:
            dfs(p, sheep, wolf, [i for i in path if i != p])

    for u, v in edges:
        graph[u].append(v)

    dfs(0, 0, 0, [])
    return answer
