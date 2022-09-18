from collections import deque
from string import ascii_uppercase


def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    board = list(map(list, zip(*board)))
    alphabet = set(list(ascii_uppercase))

    while True:
        temp = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i + 1 < len(board):
                    if len(board[i]) < j+2 or len(board[i+1]) < j+2:
                        continue
                    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                        if board[i][j] in alphabet:
                            temp.update(
                                [(i, j), (i+1, j), (i, j+1), (i+1, j+1)])

        if not temp:
            return answer

        que = deque(sorted(temp))
        answer += len(que)
        while que:
            x, y = que.pop()
            if board[x][y]:
                board[x].pop(y)

        for col in board:
            col.reverse()
