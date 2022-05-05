from itertools import combinations


def solution(orders, course):
    answer = []

    for i in course:
        set_menu = dict()
        for order in orders:
            for j in combinations(order, i):
                temp = "".join(sorted(j))
                set_menu[temp] = 0

        for order in orders:
            for j in combinations(order, i):
                temp = "".join(sorted(j))
                set_menu[temp] += 1
        if set_menu:
            res = [k for k, v in set_menu.items() if (max(set_menu.values()) == v) and (v > 1)]
            answer += res

    return sorted(answer)