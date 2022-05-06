2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
def solution(numbers, hand):
    answer = ''
    l, r = ([1, 4, 7], [3, 6, 9])
    left, right = (10, 12)
    for num in numbers:
        if num == 0:
            num = 11
        if num in l:
            answer += 'L'
            left = num
        elif num in r:
            answer += 'R'
            right = num
        else:
            mL = abs(num - left)
            mR = abs(num - right)
            dL = (mL // 3) + (mL % 3)
            dR = (mR // 3) + (mR % 3)

            if dL > dR:
                answer += 'R'
                right = num
            elif dR > dL:
                answer += 'L'
                left = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num

    return answer