from collections import defaultdict


def solution(gems):
    db = defaultdict(int)
    size = len(set(gems))
    start, end = 0, 0
    answer = [0, len(gems)]
    while end < len(gems):
        db[gems[end]] += 1
        end += 1  # 우측으로 하나씩 늘려감

        if len(db) == size:  # 보석을 일단 다 모으면
            while start < end:
                if db[gems[start]] <= 1:  # 최소 상황에 탈출
                    break
                db[gems[start]] -= 1  # 왼쪽을 한칸씩 당김
                start += 1

            # 현재 포인터 범위가 더 좁으면 초기화
            if answer[1] + 1 - answer[0] > end - start:
                answer = [start+1, end]

    return answer
