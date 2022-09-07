from itertools import combinations

def solution(relations):
    
    N = len(relations[0])
    # 전체 경우의 수
    key_idx = list(range(N))
    candidates = []
    
    for i in range(1, N+1): # 1개부터 n개까지 
        for comb in combinations(key_idx, i):
            hist = []
            for relation in relations: # row 별로
                cur = [relation[c] for c in comb] # 각 조합별로 뽑아냄
                if cur in hist: # 같은 기록이 있다면 X: 유일성
                    break
                else: # 없었다면 기록
                    hist.append(cur)
            else: # 최소성 검증
                for candidate in candidates:
                    if set(candidate).issubset(set(comb)): # 최소성을 만족하지 않는 후보키가 있다면 X
                        break
                else:
                    candidates.append(comb) 
        
    return len(candidates)
