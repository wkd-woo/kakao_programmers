from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    
    for i in range(len(q1) * 3):
        if sum1 == sum2:
            return i
        if sum1 > sum2:
            temp = q1.popleft()
            q2.append(temp)
            sum1, sum2 = sum1 - temp, sum2 + temp
        elif sum1 < sum2:
            temp = q2.popleft()
            q1.append(temp)
            sum1, sum2 = sum1 + temp, sum2 - temp

    return -1