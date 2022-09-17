from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board, skill):
    answer = 0
    row, col = len(board), len(board[0])
    for t, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if t == 1:  # 적의 공격
                    board[r][c] -= degree
                elif t == 2:  # 아군의 회복
                    board[r][c] += degree

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        cnt = 0
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]  # 상하좌우 돌면서 확인
                ny = y + dy[i]

                # 그래프 범위에서 벗어나면 생략함
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue

                if board[nx][ny] >= 1:  # 안깨졌다면
                    cnt += 1
                    board[nx][ny] = -1
                    queue.append((nx, ny))

        return cnt

    for r in range(row):
        for c in range(col):
            if board[r][c] >= 1:
                answer += 1
                board[r][c] = -1
                answer += bfs(r, c)

    return answer
