import math


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def conv(x, y):
    s = ''
    t = '0123456789ABCDEF'
    while x > 0:
        s += t[int(x % y)]
        x = int(x // y)
    s = s[::-1]
    return s


def solution(n, k):
    answer = 0
    # n을 k 진수로 변환
    if k != 10:
        k_n = conv(n, k)
    else:
        k_n = str(n)
    # 문자열 탐색 -> 소수 판별
    for i in k_n.strip().split('0'):
        if i == '':
            continue
        t = int(i)
        if is_prime_number(t) and t != 1:
            answer += 1

    return answer
