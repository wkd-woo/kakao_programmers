from string import ascii_uppercase
from collections import deque

def solution(msg):
    answer, msg = [], deque(msg)
    alphabet_list = list(ascii_uppercase)
    db = {alphabet:i+1 for i, alphabet in enumerate(alphabet_list)}
    last, s = 26, ''
    while msg:
        s += msg.popleft()
        if not msg:
            answer.append(db[s])
            
        elif s + msg[0] not in db:
            last += 1
            answer.append(db[s])
            db[s + msg[0]] = last
            s = ''
            continue
    
    return answer