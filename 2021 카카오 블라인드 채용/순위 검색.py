from itertools import combinations


def solution(info, query):
    answer, db = [], {}
    for i in info: # 각 지원자
        temp = i.split() # 
        conditions = temp[:-1] # 조건 모음
        score = int(temp[-1]) # 점수
        for n in range(5):
            for c in list(combinations(range(4), n)):
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]
                
    for value in db.values():
        value.sort()
        
    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        
        if qry_cnd in db:
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end:
                    mid = (start + end) // 2
                    if data[mid] >= qry_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)
                
    return answer