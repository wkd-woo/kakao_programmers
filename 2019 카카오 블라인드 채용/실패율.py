def solution(N, stages):
    record = dict()
    failure_rate = dict()
    for i in range(1, N + 1):
        record[i] = [0, 0]  # 도전자, 실패자
        failure_rate[i] = 0  # 실패율 결과

    for stage in stages:
        if stage == N + 1:  # N+1이면
            for i in range(1, N + 1):  # 올 클리어
                record[i][0] += 1
        else:
            for i in range(1, stage + 1):
                record[i][0] += 1  # 현재 stage 이전까지 모두 도전했고
            record[stage][1] += 1  # 현재 stage만 실패

    for r in record:  # 기록
        if not record[r][1]:  # 실패자가 없으면
            failure_rate[r] = 0  # 실패율 0
        else:
            failure_rate[r] = record[r][1] / record[r][0]
    # 실패율 순으로 내림차순 정렬
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)
