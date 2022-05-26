import re

static = 65536


def solution(str1, str2):
    # 대소문자 무시
    str1 = str1.lower()
    str2 = str2.lower()

    # A, B 합집합 크기를 찾음
    ## 두개 다 있을 때, 교집합은 작은거, 합집합은 큰거
    A = dict()
    B = dict()
    union = dict()

    # 두 글자씩 끊어서 다중 집합의 원소로 만듬
    for i in range(0, len(str1)):
        if i == len(str1) - 1:
            continue
        # 공백, 숫자, 특수문자가 들어있으면 글자 쌍 버림
        temp = re.sub('[^a-zA-Z]', '', str1[i:i + 2])
        if len(temp) < 2:
            continue

        if temp not in A:
            A[temp] = 1
        else:
            A[temp] += 1

    for i in range(0, len(str2)):
        if i == len(str2) - 1:
            continue
        temp = re.sub('[^a-zA-Z]', '', str2[i:i + 2])
        if len(temp) < 2:
            continue

        if temp not in B:
            B[temp] = 1
        else:
            B[temp] += 1

    intersection = dict()  # 교집합

    for each in A:
        union[each] = A[each]
        if each in B:
            intersection[each] = min(A[each], B[each])  # 교집합은 둘 중 개수가 적은 것

    for each in B:
        if each not in union:
            union[each] = B[each]
        else:
            union[each] = max(B[each], union[each])  # 합집합은 둘 중 개수가 큰 것

    if union:
        answer = int((sum(intersection.values()) / sum(union.values())) * static)
    else:  # 집합 A와 집합 B가 모두 공집합
        answer = static
    return answer
