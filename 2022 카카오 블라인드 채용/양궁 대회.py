from itertools import combinations_with_replacement


def solution(n, infos):
    answer = [-1]
    mx = -int(1e9)
    candidates = list(combinations_with_replacement(range(0, 11), n))  # 중복조합

    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0

        for score in candidate:  # 점수 맞출 때 마다 +1
            info2[10-score] += 1

        for score, (a, l) in enumerate(zip(infos, info2)):
            if a == l == 0:  # 둘 다 못맞췄으면 PASS
                continue
            elif a >= l:  # 어피치가 해당 점수를 더 많이 맞추거나, 같은 점수를 맞추면 어피치에게 점수
                apeach += (10 - score)
            else:  # 라이언이 해당 점수를 더 많이 맞추면 라이언에게 점수
                lion += (10 - score)

        if lion > apeach:  # 라이언이 더 많이 맞춘 경우에
            gap = lion - apeach
            if gap > mx:  # 기존 차이보다 크면 초기화
                mx = gap
                answer = info2

    return answer
