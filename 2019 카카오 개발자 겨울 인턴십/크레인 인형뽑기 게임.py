def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for i in range(len(board)):  # 위에서부터 내려감
            if board[i][move - 1]:  # 만약 값이 있으면
                temp = board[i][move - 1]  # 뽑아서

                if not stack:  # stack에 아무것도 없는 경우
                    stack.append(temp)

                else:  # stack에 무언가 들어있는 경우
                    if stack[-1] == temp:  # stack 맨 위가 temp와 같으면
                        answer += 2  # answer에 2 더하고
                        stack.pop()  # stack 맨 위값을 pop
                    else:  # stack 맨 위가 temp와 다르면
                        stack.append(temp)  # temp를 넣는다

                board[i][move - 1] = 0  # 뽑았으니 없앰
                break

    return answer
