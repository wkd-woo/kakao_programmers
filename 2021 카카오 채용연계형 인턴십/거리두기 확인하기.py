from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 'P':  # P 발견하면 실패
                return False

            elif graph[nx][ny] == 'O':  # O 발견하면 한번 더 탐색
                for i in range(4):
                    mx = nx + dx[i]  # 상하좌우 돌면서 확인
                    my = ny + dy[i]

                    # 그래프 범위에서 벗어나면 생략함
                    if mx < 0 or mx >= n or my < 0 or my >= n:
                        continue

                    if mx == x and my == y:
                        continue

                    if graph[mx][my] == 'P':  # P 발견하면 실패
                        return False

    return True


def solution(places):
    answer = []
    for place in places:
        graph = [list(row) for row in place]
        cond = True
        for i in range(len(place)):
            for j in range(len(place)):
                if graph[i][j] == 'P':
                    cond = bfs(graph, i, j)
                if not cond:
                    answer.append(0)
                    break
            if not cond:
                break
        if cond:
            answer.append(1)
    return answer
